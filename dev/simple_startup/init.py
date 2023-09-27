###### THIS IS A LITTLE OLD 
######### BUT THE BASIC IDEA IS IT CREATES A CHOLINE.JSON FILE FOR CREATING INSTANCES EASILY 



import argparse
import subprocess
import os
import sys
import json 


import shutil
from datetime import datetime

# def late_init_command_for_choline_launch():
#     image_name, gpu_filters = None, None 
#     if image_name is None:
#         image_name = input("Enter the Docker image name (default is pytorch/pytorch): ") or 'pytorch/pytorch'
        
    
#     if gpu_filters is None:
#         gpu_filters = input("Enter GPU filters for Vast.ai: ")

#     checkpoint_locations, copy_locations = create_upload_dirs()
#     start_cmd = create_run_cmd()
    
#     create_choline_json(image_name, checkpoint_locations, copy_locations, start_cmd, gpu_filters)

# from cho_createv2 import create_command
######################### on hold for now 
# def create_dockerfile(choline_dir):
#     local_cuda_version = get_local_cuda_version()
#     local_python_version = get_python_version()
#     req_list = get_requirements_list()
#     conda_version = get_conda_version()
    
#     dockerfile_path = os.path.join(choline_dir, "Dockerfile")
#     dockerfile_lines = [
#         f"FROM conda/miniconda3-cuda{local_cuda_version}-cudnn8-runtime:{conda_version}",
#         f"ENV PYTHON_VERSION={local_python_version}",
#         "WORKDIR /workspace",
#         "RUN conda install -y python=${PYTHON_VERSION}",
#         "RUN conda install -y pip",
#     ] + [f"RUN pip install {req}" for req in req_list]
    
#     with open(dockerfile_path, 'w') as file:
#         file.write('\n'.join(dockerfile_lines))
######################### on hold for now 



def get_local_cuda_version():
    try:
        result = subprocess.run(["nvcc", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result.check_returncode()
        version_line = result.stdout.decode().split("\n")[-2]
        local_cuda_version = version_line.split("_")[1].split(".r")[0]
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("CUDA not found. Using default version 12.0.")
        local_cuda_version = '12.0'
    return local_cuda_version

def get_python_version():
    return sys.version.split(' ')[0]

def get_requirements_list():
    result = subprocess.run(["pip", "freeze"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Error getting requirements. Using empty requirements.")
        return []
    return result.stdout.decode().split("\n")

def get_conda_version():
    try:
        result = subprocess.run(["conda", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result.check_returncode()
        conda_version = result.stdout.decode().strip().split(" ")[-1]
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Conda not found. Using 'latest' as default.")
        conda_version = 'latest'
    return conda_version



def create_choline_json(image_name, checkpoint_locations, direct_copy_locations, start_cmd, gpu_name,disk_space):
    choline_json = {
        "image": image_name,
        # "checkpoint_upload_locations": checkpoint_locations,
        "upload_locations": direct_copy_locations,
        "onStart": start_cmd,
        "local_cuda_version": get_local_cuda_version(),
        "python_version": get_python_version(),
        "requirements": get_requirements_list(),
        "conda_version": get_conda_version(),
        "hardware_filters": {"gpu_name": gpu_name, "disk_space":disk_space}
    }
    
    with open('choline.json', 'w') as f:
        json.dump(choline_json, f, indent=4)


# def create_upload_dirs():
#     add_cwd = input("Add entire current working directory? (y/n): ").strip().lower()
#     locations = []
#     if add_cwd == 'y':
#         locations.append(os.getcwd())
#     additional_locations = input("Enter additional locations to upload (comma-separated,no spaces): ").split(',')
#     locations.extend(additional_locations)
#     return locations


# #### added in checkpointed vs static 
# def create_upload_dirs():
#     # For checkpointed files
#     # add_cwd_checkpoint = input("Add entire current working directory to checkpointed files? (y/n): ").strip().lower()
#     # checkpoint_locations = []
#     # if add_cwd_checkpoint == 'y':
#     #     checkpoint_locations.append(os.getcwd())
#     # additional_checkpoint_locations = input("Enter additional locations to upload as checkpointed (comma-separated, no spaces): ").split(',')
#     # checkpoint_locations.extend(additional_checkpoint_locations)
    
#     # For directly copied files
#     add_cwd_copy = input("Add entire current working directory to directly copied files? (y/n): ").strip().lower()
#     copy_locations = []
#     if add_cwd_copy == 'y':
#         copy_locations.append(os.getcwd())
#     additional_copy_locations = input("Enter additional locations to upload as directly copied (comma-separated, no spaces): ").split(',')
#     copy_locations.extend(additional_copy_locations)
    
#     return 0, copy_locations

def create_upload_dirs():
    # For checkpointed files
    # add_cwd_checkpoint = input("Add entire current working directory to checkpointed files? (y/n): ").strip().lower()
    # checkpoint_locations = []
    # if add_cwd_checkpoint == 'y':
    #     checkpoint_locations.append(os.getcwd())
    # additional_checkpoint_locations = input("Enter additional locations to upload as checkpointed (comma-separated, no spaces): ").split(',')
    # checkpoint_locations.extend(additional_checkpoint_locations)
    
    # For directly copied files
    add_cwd_copy = input("Add entire current working directory to directly copied files? (y/n): ").strip().lower()
    copy_locations = []
    if add_cwd_copy == 'y':
        copy_locations.append(os.getcwd())
    additional_copy_locations_input = input("Enter additional locations to upload as directly copied (comma-separated, no spaces): ")
    if additional_copy_locations_input.strip():
        additional_copy_locations = additional_copy_locations_input.split(',')
        copy_locations.extend(additional_copy_locations)
    
    return 0, copy_locations


def create_run_cmd():
    tr_command = input("Enter the train command after setting up your instance: ")
    return tr_command


def ask_for_gpu_choice():
    gpu_choices = [
        'RTX_3060', 'H100', 'H100 PCIE', 'A100', 'RTX_3080', 'RTX_3090', 'A100 SXM4',
        'RTX_A5000', 'RTX_4090', 'RTX_3070', 'Tesla_V100', 'A401', 'RTX_3090',
        'RTX_A4000'
    ]
    print("Available GPUs:")
    for idx, choice in enumerate(gpu_choices):
        print(f"{idx}. {choice}")
    selected_idx = int(input("Enter the number corresponding to your choice: "))
    return gpu_choices[selected_idx]

def ask_for_image_choice():
    image_choices = [
        'pytorch/pytorch',
        'tensorflow/tensorflow',
        'nvidia/cuda:12.0.0-devel-ubuntu20.04',
        'ubuntu:latest',
        'alpine:latest'
    ]
    print("Available Images:")
    for idx, choice in enumerate(image_choices):
        print(f"{idx}. {choice}")
    selected_idx = int(input("Enter the number corresponding to your choice: "))
    return image_choices[selected_idx]




def ask_for_disk_space():
    disk_space = input("Enter the amount of disk space needed (in GB): ")
    return f">{disk_space}"


def init_command():
    image = ask_for_image_choice()
    removed, copy_locations = create_upload_dirs()
    start_cmd = create_run_cmd()
    gpu_filters = ask_for_gpu_choice()
    disk_space = ask_for_disk_space()
    create_choline_json(image, removed, copy_locations, start_cmd, gpu_filters, disk_space)






# def main():
#     parser = argparse.ArgumentParser(description='Choline commands.')
#     subparsers = parser.add_subparsers()
    
#     parser_init = subparsers.add_parser('init')
#     parser_init.add_argument('--image', required=False, help='Name of the Docker image', default='pytorch/pytorch')
#     parser_init.add_argument('--gpu_filters', required=False, type=str, help='Price and parameter filters for reserving instances on Vast.ai')
#     parser_init.set_defaults(func=init_command)

#     parser_create = subparsers.add_parser('create')

#     parser_create.set_defaults(func=create_command)  # Import cho_create at the top

#     args = parser.parse_args()
#     args.func(args)

if __name__ == '__main__':
    init_command()