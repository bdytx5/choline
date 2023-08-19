
################################################################################
# Author: Brett Young                                                          #
# Date: 8/18/23                                                                #
# Organization: Choline (not yet incorporated the company)                     #
#                                                                              #
# Description:                                                                 #
# This script is designed to automate the process of finding and reserving     #
# instances with specific GPU and driver properties that match the current     #
# system. Usage: `python instance_creator.py GPU_VERSION`, e.g., 3090.         #
################################################################################

# DOCS 

# This script is designed to automate the process of finding and reserving instances with specific
# GPU and driver properties that match the current system. The script takes the GPU version (e.g., "3090")
# as a command-line argument and fetches the local CUDA version. It then searches for offers containing
# instances that match the given GPU version and are compatible with the local CUDA version. 
# The instances are further sorted by how close their driver version is to the local driver version, with
# the conversion of driver version to integers for comparison. The sorted list of instances is displayed 
# in reverse order in the terminal, allowing the user to select an instance to reserve. The instance 
# creation includes options such as image and disk space, and a success or error message is printed
# accordingly. To use the script, simply run it with the desired GPU version as an argument, like so:
#  python instance_creator.py 3090.






import subprocess
import json

import subprocess
import json
import sys

def convert_version_to_int(version_str):
    return int(version_str.replace('.', ''))

def sort_offers_by_driver_and_gpu(offers, target_gpu, target_driver_version):
    # Filter offers that include the specified GPU version
    filtered_offers = [offer for offer in offers if target_gpu in offer['gpu_name']] # Assuming 'gpu_name' contains GPU version

    target_driver_version_int = convert_version_to_int(target_driver_version)

    # Sort offers by how close their driver version is to the local driver version
    sorted_offers = sorted(filtered_offers, key=lambda x: abs(convert_version_to_int(x['driver_version']) - target_driver_version_int)) # Assuming 'driver_version' contains driver version
    return sorted_offers


import subprocess

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


def search_offers(cuda_version):
    query = f"cuda_vers == {cuda_version}"
    command = ["vastai", "search", "offers", "--raw", query]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Error in search:", result.stderr.decode())
        return []

    offers = json.loads(result.stdout.decode())
    return offers

def create_instance(instance_id, options):
    command = ["./vast", "create", "instance", str(instance_id)] + options
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Error in instance creation:", result.stderr.decode())
        return None
    
    print("Instance created successfully:", result.stdout.decode())
    return result.stdout.decode()


target_gpu = sys.argv[1]
local_driver_version = get_local_driver_version()
local_cuda_version = get_local_cuda_version()
offers = search_offers(local_cuda_version)

if offers:
    # Assuming the sorted_offers are obtained as shown in the previous example
    sorted_offers = sort_offers_by_driver_and_gpu(offers, target_gpu, local_driver_version)

    if sorted_offers:
        print("Compatible instances:")
        for i, offer in enumerate(sorted_offers[::-1]): # Reverse the list by using [::-1]
            print(f"{i}: Instance ID: {offer['id']}, CUDA Version: {offer['cuda_max_good']}, GPUs: {offer['num_gpus']}, Driver Version: {offer['driver_version']}") # Included Driver Version

        choice = int(input("Enter the index of the instance you want to use: "))
        if 0 <= choice < len(sorted_offers):
            instance_id = sorted_offers[::-1][choice]["id"] # Reverse the list here as well
            options = ["--image", "bobsrepo/pytorch:latest", "--disk", "20"]
            create_instance(instance_id, options)
        else:
            print("Invalid choice. Exiting.")
    else:
        print("No suitable offers found.")
