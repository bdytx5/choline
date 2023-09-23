# this will read machine params like GPU and Storage params from the choline json, and then ask u to select an instance 
# then it will use the software env info in the choline.json file to create an onstart script to set up the environment 
## then it will monitor the status of that machine and alert u if it fails 
import os
import json
import subprocess
import time
import argparse
import argparse
import os
import subprocess
import json
import torch
import re 




def get_choline_json_data():
    with open('./choline.json', 'r') as f:
        return json.load(f)




def custom_sort_key(offer, expected_storage_gb, expected_runtime_hr, expected_upload_gb=1.0):
    dph = offer['dph_base']
    storage_cost_per_hr = (offer['storage_cost'] / (30 * 24)) * expected_storage_gb
    total_storage_cost = storage_cost_per_hr * expected_runtime_hr
    download_cost = expected_storage_gb * offer['inet_down_cost']
    upload_cost = expected_upload_gb * offer['inet_up_cost']
    total_cost = (dph + storage_cost_per_hr) * expected_runtime_hr + download_cost + upload_cost
    
    return total_cost




def sort_offers_by_custom_criteria(offers, expected_storage_gb, expected_runtime_hr):
    return sorted(offers, key=lambda x: custom_sort_key(x, expected_storage_gb, expected_runtime_hr))




def pretty_print_offer(offer, index):
    print(f"########### VASTAI OFFERS {index + 1} ###########")
    print(f"Cost per hour: {offer['dph_base']}")
    print(f"Internet download speed: {offer['inet_down']}")
    print(f"Internet upload speed: {offer['inet_up']}")
    print(f"DL Performance: {offer['dlperf']}")
    print(f"Reliability: {offer['reliability2']}")
    print(f"Storage cost: {offer['storage_cost']}")
    print(f"Internet download cost: {offer['inet_down_cost']}")
    print(f"Internet upload cost: {offer['inet_up_cost']}")
    print("#######################################\n\n")



def generate_onstart_script():
    choline_data = get_choline_json_data()
    python_version = choline_data.get("python_version", "3.8")
    requirements = choline_data.get("requirements", [])

    with open("./choline_onstart.sh", "w") as f:
        f.write("#!/bin/bash\n")
        f.write(f"conda create --name myenv python={python_version}\n")
        f.write("source activate myenv\n")

        for package in requirements:
            f.write(f"conda install {package} --yes\n")

        f.write("echo 'Environment setup complete'\n")

    


#### LOOKS LIKE THERE IS A SIZE LIMIT FOR THE SH SCRIPT, SO WE WILL NEED TO MAKE OUR OWN SETUP ....
def generate_onstart_script():
    choline_data = get_choline_json_data()
    python_version = choline_data.get('python_version', '3.8')
    requirements = choline_data.get('requirements', [])    

    script_lines = [
        "#!/bin/bash",
        "# Download Miniconda installer",
        "wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh",
        "# Install Miniconda",
        "bash miniconda.sh -b -p $HOME/miniconda",
        "# Initialize conda",
        "source $HOME/miniconda/bin/activate",
        "conda init",
        "# Create environment",
        f"conda create --name myenv python={python_version} -y",
        "# Activate environment",
        "conda activate myenv",
    ]

    # Add lines to install required packages
    for pkg in requirements:
        script_lines.append(f"conda install {pkg} -y || pip install {pkg}")

    script_content = "\n".join(script_lines)

    # Save the script to a file
    with open("choline_onStart.sh", "w") as f:
        f.write(script_content)

    return "./choline_onStart.sh"




def search_offers(additional_query=""):
    # query = f"cuda_vers == {cuda_version}"
    query = f""
    if additional_query:
        query = f"{query} {additional_query}"

    command = ["vastai", "search", "offers", "--raw", query]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Error in search:", result.stderr.decode())
        return []
    
    offers = json.loads(result.stdout.decode())
    return offers




def create_instance(instance_id, options):
    command = ["vastai", "create", "instance", str(instance_id)] + options
    print(command)
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("res {}".format(result))
    if result.returncode != 0:
        print("Error in instance creation:", result.stderr.decode())
        return None
    print(f"Instance created successfully.")




def main():
    choline_data = get_choline_json_data()
    hardware_filters = choline_data.get('hardware_filters', {})
    gpu_name = hardware_filters.get('gpu_name', '')
    disk_space_str = hardware_filters.get('disk_space', '')
    image = choline_data.get('image', 'python:3.8')
    # startup_script_path = generate_onstart_script()

    startup_script_path = "./choline_onStart.sh"

    # Extract operator and value from the disk_space string
    match = re.match(r"([<>!=]+)(\d+)", disk_space_str)
    if match:
        disk_space_operator, disk_space_value = match.groups()
        disk_space_value = int(disk_space_value)
    else:
        print("Invalid disk_space string in JSON. Using default values.")
        return 

    query = f"gpu_name={gpu_name} disk_space {disk_space_operator} {disk_space_value}"
    print(query)
    offers = search_offers(query)
    exp_storage = disk_space_value

    offers = sort_offers_by_custom_criteria(offers, expected_storage_gb=exp_storage, expected_runtime_hr=2)

    if offers:
        print("Five cheapest offers:")
        for i, offer in enumerate(offers[:5]):
            pretty_print_offer(offer, i)

        choice = int(input("Select an offer by entering its number (1-5): ")) - 1
        selected_offer = offers[choice]
        pretty_print_offer(selected_offer, choice)

        confirmation = input("Would you like to proceed? (y/n): ")
        if confirmation.lower() == 'y':
            instance_id = selected_offer["id"]
            options = ["--image", image, "--disk", str(disk_space_value), "--onstart", startup_script_path, "--env", "-e TZ=PDT -e XNAME=XX4 -p 22:22 -p 8080:8080"]
            create_instance(instance_id, options)

            print(f"Instance creation request complete. Now setting up your instance with id {instance_id}. Run 'choline status 'instance id'' to check the logs for your setup.")
        else:
            print("Operation canceled.")
    else:
        print("No suitable offers found.")

if __name__ == "__main__":
    main()
