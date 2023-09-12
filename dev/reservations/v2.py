import argparse
import os
import subprocess
import json
import sys
from build_dockerfile import create_docker_file_from_env

def convert_version_to_int(version_str):
    return int(version_str.replace('.', ''))

def get_size_cost(size_gb, inet_up_cost, inet_down_cost):
    upload_cost = size_gb * inet_up_cost
    download_cost = size_gb * inet_down_cost
    return upload_cost, download_cost

def sort_offers_by_driver_and_gpu(offers, target_gpu, target_driver_version, size_gb, storage_price, max_price=None):
    filtered_offers = [offer for offer in offers if target_gpu in offer['gpu_name']]
    target_driver_version_int = convert_version_to_int(target_driver_version)
    sorted_offers = sorted(filtered_offers, key=lambda x: (abs(convert_version_to_int(x['driver_version']) - target_driver_version_int), x['dph_total'] + storage_price * size_gb))

    for offer in sorted_offers:
        upload_cost, download_cost = get_size_cost(size_gb, float(offer['inet_up_cost']), float(offer['inet_down_cost']))
        offer['upload_cost'] = upload_cost
        offer['download_cost'] = download_cost

    if max_price is not None:
        sorted_offers = [offer for offer in sorted_offers if offer['dph_total'] <= max_price]

    if sorted_offers:
        cheapest_offer = min(sorted_offers, key=lambda x: x['dph_total'])
        return [cheapest_offer]

    return sorted_offers

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

def search_offers(cuda_version):
    query = f"cuda_vers == {cuda_version}"
    command = ["vastai", "search", "offers", "--raw", query]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Error in search:", result.stderr.decode())
        return []

    offers = json.loads(result.stdout.decode())
    return offers

def create_instance(instance_id, options, size_gb, upload_price, download_price):
    command = ["vastai", "create", "instance", str(instance_id)] + options
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Error in instance creation:", result.stderr.decode())
        return None

    upload_cost = size_gb * upload_price
    download_cost = size_gb * download_price
    print(f"Instance created successfully. Upload cost for {size_gb} GB: ${upload_cost}. Download cost for {size_gb} GB: ${download_cost}.")

def onstart_script_path(dockerfile_path):
    script_content = f"""#!/bin/bash
    # Commands to copy the Dockerfile from the project's root directory
    cp {dockerfile_path} /destination/path/

    # Commands to install Vim
    apt-get update && apt-get install -y vim
    """
    script_path = "/path/to/your_script.sh"
    with open(script_path, 'w') as file:
        file.write(script_content)
    os.chmod(script_path, 0o755)  # Make the script executable
    return script_path

def main():
    parser = argparse.ArgumentParser(description="Instance Creator")
    parser.add_argument('--gpu', required=True, help='GPU identifier')
    parser.add_argument('--size', required=False, type=int, help='Size in GB')
    parser.add_argument('--upload-price', required=True, type=float, help='Upload price')
    parser.add_argument('--download-price', required=True, type=float, help='Download price')
    parser.add_argument('--storage-price', required=True, type=float, help='Storage price')
    args = parser.parse_args()

    target_gpu = args.gpu
    size_gb = args.size if args.size else get_current_directory_size()
    upload_price = args.upload_price
    download_price = args.download_price
    storage_price = args.storage_price

    local_driver_version = get_local_driver_version()
    local_cuda_version = get_local_cuda_version()
    offers = search_offers(local_cuda_version)

    if offers:
        sorted_offers = sort_offers_by_driver_and_gpu(offers, target_gpu, local_driver_version, size_gb, storage_price)

        if sorted_offers:
            print("Compatible instances:")
            for i, offer in enumerate(sorted_offers[::-1]):
                print(f"{i}: Instance ID: {offer['id']}, CUDA Version: {offer['cuda_max_good']}, GPUs: {offer['num_gpus']}, Driver Version: {offer['driver_version']}, Upload Cost for {size_gb} GB: ${offer['upload_cost']}, Download Cost for {size_gb} GB: ${offer['download_cost']}")

            choice = int(input("Enter the index of the instance you want to use: "))
            if 0 <= choice < len(sorted_offers):
                instance_id = sorted_offers[::-1][choice]["id"]
                options = ["--image", "bobsrepo/pytorch:latest", "--disk", "20"]
                onstart_script = onstart_script_path(create_docker_file_from_env())
                options += ["--onstart", onstart_script]
                create_instance(instance_id, options, size_gb, upload_price, download_price)
            else:
                print("Invalid choice. Exiting.")
        else:
            print("No suitable offers found.")

if __name__ == "__main__":
    main()