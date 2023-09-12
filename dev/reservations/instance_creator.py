import argparse
import os
import subprocess
import json
import sys
from build_dockerfile import create_docker_file_from_env
import time 

def convert_version_to_int(version_str):
    return int(version_str.replace('.', ''))

def sort_offers_by_driver_and_gpu(offers):

    filtered_offers = offers # user now filters using stock vast cli 
    sorted_and_filtered_offers = sorted(filtered_offers, key=lambda x: x['dph_total'])

    return sorted_and_filtered_offers


def get_local_driver_version():
    try:
        result = subprocess.run(["nvidia-smi", "--query-gpu=driver_version", "--format=csv,noheader,nounits"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result.check_returncode()
        local_driver_version = result.stdout.decode().strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("NVIDIA driver not found on this machine. Using default version.")
        local_driver_version = "525.60.11"
    return local_driver_version

def get_local_cuda_version():
    try:
        result = subprocess.run(["nvcc", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result.check_returncode()
        version_line = result.stdout.decode().split("\n")[-2]
        local_cuda_version = version_line.split(" ")[-1]
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("CUDA not found on this machine. Using version 12.0 as default.")
        local_cuda_version = '12.0'
    return local_cuda_version

def get_current_directory_size():
    total_size = 0
    for dirpath, dirnames, filenames in os.walk('.'):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return (total_size / (1024 ** 3)) + 10  # Convert to GB and add 10 GB

# 'make the requirements less dumb' - Elon 
def search_offers(cuda_version, additional_query=""):
    query = f"cuda_vers == {cuda_version}"
    
    if additional_query:
        query = f"{query} {additional_query}"

    command = ["vastai", "search", "offers", "--raw", query]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Error in search:", result.stderr.decode())
        return []

    offers = json.loads(result.stdout.decode())
    return offers


def create_instance(instance_id, options, size_gb, storage_cost):
    # can supply --image as well as storage 
    command = ["vastai", "create", "instance", str(instance_id)] + options
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Error in instance creation:", result.stderr.decode())
        return None

    upload_cost, download_cost, storage_cost_total = get_costs(size_gb, float(result.stdout.decode()['inet_up_cost']), float(result.stdout.decode()['inet_down_cost']), storage_cost)
    print(f"Instance created successfully. Upload cost for {size_gb} GB: ${upload_cost}. Download cost for {size_gb} GB: ${download_cost}. Storage cost for {size_gb} GB: ${storage_cost_total}.")

def onstart_script_path(dockerfile_path):
    script_content = f"""#!/bin/bash
    cp {dockerfile_path} /destination/path/
    apt-get update && apt-get install -y vim
    """
    script_path = "/path/to/your_script.sh"
    with open(script_path, 'w') as file:
        file.write(script_content)
    os.chmod(script_path, 0o755)  # Make the script executable
    return script_path

def main():
    parser = argparse.ArgumentParser(description="Instance Creator")
    parser.add_argument('--query', required=True, help='Query for filtering offers')
    
    args = parser.parse_args()

    query = args.query

    local_driver_version = get_local_driver_version()
    local_cuda_version = get_local_cuda_version()
    offers = []
    
    while not offers:
        offers = search_offers(local_cuda_version, query)
        if not offers:
            print("No suitable offers found. Checking again in 30 seconds.")
            time.sleep(30)

    sorted_offers = sort_offers_by_criteria(offers, query)

    if sorted_offers:
        instance_id = sorted_offers[0]["id"]
        options = ["--image", "bobsrepo/pytorch:latest", "--disk", "20"]
        onstart_script = onstart_script_path(create_docker_file_from_env())
        options += ["--onstart", onstart_script]
        create_instance(instance_id, options)
    else:
        print("No suitable offers found.")

if __name__ == "__main__":
    main()



#     target_gpu = args.gpu
#     size_gb = args.size if args.size else get_current_directory_size()
#     storage_cost = args.storage_cost
#     inet_up_max_cost = args.inet_up_max_cost
#     inet_down_max_cost = args.inet_down_max_cost

#     local_driver_version = get_local_driver_version()
#     local_cuda_version = get_local_cuda_version()
#     offers = search_offers(local_cuda_version)

#     if offers:
#         sorted_offers = sort_offers_by_driver_and_gpu(offers, target_gpu, local_driver_version, size_gb=size_gb, storage_cost=storage_cost, inet_up_max_cost=inet_up_max_cost, inet_down_max_cost=inet_down_max_cost, max_dph_price=args.max_dph_price)  # Updated function call


#         # if sorted_offers:
#         #     print("Compatible instances:")
#         #     for i, offer in enumerate(sorted_offers):
#         #         print(f"{i}: Instance ID: {offer['id']}, DPH_COST {offer['dph_total']} CUDA Version: {offer['cuda_max_good']}, GPUs: {offer['num_gpus']}, Driver Version: {offer['driver_version']}, Upload Cost for {size_gb} GB: ${offer['inet_up_cost']:.6f}, Download Cost for {size_gb} GB: ${offer['inet_down_cost']*size_gb:.6f}, Storage Cost for {size_gb} GB: ${offer['storage_cost']*size_gb:.6f}")

#         #     choice = int(input("Enter the index of the instance you want to use: "))
#         #     if 0 <= choice < len(sorted_offers):
#         #         instance_id = sorted_offers[::-1][choice]["id"]
#         #         options = ["--image", "bobsrepo/pytorch:latest", "--disk", "20"]
#         #         onstart_script = onstart_script_path(create_docker_file_from_env())
#         #         options += ["--onstart", onstart_script]
#         #         create_instance(instance_id, options, size_gb, storage_cost)
#         #     else:
#         #         print("Invalid choice. Exiting.")
#         # else:
#         #     print("No suitable offers found.")

#         # Automatically choose the first instance in the sorted list
#         if sorted_offers:
#             instance_id = sorted_offers[0]["id"]
#             options = ["--image", "bobsrepo/pytorch:latest", "--disk", "20"]
#             onstart_script = onstart_script_path(create_docker_file_from_env())
#             options += ["--onstart", onstart_script]
#             create_instance(instance_id, options, size_gb, storage_cost)
#         else:
#             print("No suitable offers found.")


# if __name__ == "__main__":
#     main()






# def search_offers(cuda_version):
#     query = f"cuda_vers == {cuda_version}"
#     command = ["vastai", "search", "offers", "--raw", query]
#     result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     if result.returncode != 0:
#         print("Error in search:", result.stderr.decode())
#         return []

#     offers = json.loads(result.stdout.decode())
#     return offers


# def get_costs(size_gb, inet_up_cost, inet_down_cost, storage_cost):
#     upload_cost = size_gb * inet_up_cost
#     download_cost = size_gb * inet_down_cost
#     storage_cost_total = size_gb * storage_cost
#     return upload_cost, download_cost, storage_cost_total




# def sort_offers_by_driver_and_gpu(offers, target_gpu, target_driver_version, size_gb, storage_cost, inet_up_max_cost, inet_down_max_cost, max_dph_price):

#     print(f"Searching for offers with the following parameters:\n"
#         f"Target GPU: {target_gpu}\n"
#         f"Target Driver Version: {target_driver_version}\n"
#         f"Size (in GB): {size_gb}\n"
#         f"Storage Cost (in dollars): {storage_cost}\n"
#         f"Max Upload Cost (in dollars): {inet_up_max_cost}\n"
#         f"Max Download Cost (in dollars): {inet_down_max_cost}\n"
#         f"Max DPH Price (in dollars): {max_dph_price}\n")

#     filtered_offers = []
#     for offer in offers:
#         if target_gpu in offer['gpu_name'] and float(offer['dph_total']) <= max_dph_price and float(offer['storage_cost']) <= storage_cost:
#             if offer['inet_up_cost'] <= inet_up_max_cost and offer['inet_down_cost'] <= inet_down_max_cost:  ## 13 inch mb air 
#                 filtered_offers.append(offer)

#     target_driver_version_int = convert_version_to_int(target_driver_version)
#     sorted_and_filtered_offers = []

#     # for offer in filtered_offers:
#     #     upload_cost, download_cost, storage_cost_total = get_costs(size_gb, float(offer['inet_up_cost']), float(offer['inet_down_cost']), storage_cost)

#     #     if upload_cost <= inet_up_max_cost and download_cost <= inet_down_max_cost and storage_cost_total <= storage_cost:
#     #         offer['upload_cost'] = upload_cost
#     #         offer['download_cost'] = download_cost
#     #         offer['storage_cost'] = storage_cost_total
#     #         sorted_and_filtered_offers.append(offer)

#     sorted_and_filtered_offers = sorted(filtered_offers, key=lambda x: x['dph_total'])

#     return sorted_and_filtered_offers

