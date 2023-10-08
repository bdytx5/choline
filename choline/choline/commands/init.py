
import argparse
import subprocess
import os
import sys
import json 
from pathlib import Path

import yaml 
import shutil
from datetime import datetime


import os
import fnmatch

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


def get_conda_version():
    try:
        result = subprocess.run(["conda", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result.check_returncode()
        conda_version = result.stdout.decode().strip().split(" ")[-1]
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Conda not found. Using 'latest' as default.")
        conda_version = 'latest'
    return conda_version



def get_requirements_list():
    result = subprocess.run(["pip", "freeze"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Error getting requirements. Using empty requirements.")
        return []
    return result.stdout.decode().split("\n")



def get_requirements_list():
    while True:
        use_req_txt = input("Do you want to supply the path to a requirements.txt file? (y/n): ").lower()
        
        if use_req_txt == 'y':
            req_path = input("Please enter the full path to your requirements.txt file: ")
            
            if os.path.exists(req_path):
                with open(req_path, 'r') as f:
                    return f.read().split("\n")
            else:
                print("The provided path does not exist.")
                
                while True:
                    continue_or_quit = input("Do you want to reenter the path or use pip freeze? (reenter/pip): ").lower()
                
                    if continue_or_quit == 'pip':
                        break
                    elif continue_or_quit == 'reenter':
                        break
                    else:
                        print("Invalid option. Please choose 'reenter' or 'pip'.")
                
                if continue_or_quit == 'pip':
                    break
        elif use_req_txt == 'n':
            break
        else:
            print("Invalid option. Please choose 'y' or 'n'.")
            continue
    
    result = subprocess.run(["pip", "freeze"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode != 0:
        print("Error getting requirements. Using empty requirements.")
        return []
    
    return result.stdout.decode().split("\n")


def get_python_version():
    return sys.version.split(' ')[0]



from pathlib import Path
import yaml



def create_setup_script(wndb_key, on_start_cmd):
    python_version = get_python_version()
    setup_script_content = f'''#!/bin/bash
# Download Miniconda installer
# wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
# Install Miniconda
# bash miniconda.sh -b -p $HOME/miniconda
# Initialize conda
# . $HOME/miniconda/bin/activate
# conda init
# Create environment
# conda create --name choline python={python_version} -y
# Activate environment
# conda activate choline
# Install vim
export cholineremote=true
sudo apt upgrade
sudo apt install vim -y
sudo apt install python3 -y
sudo apt install python3-pip -y
# Set Wandb API key without user interaction
export WANDB_API_KEY={wndb_key}
'''

    requirements = get_requirements_list()
    for req in requirements:
        setup_script_content += f'pip install {req} || pip3 install {req} -y\n'
        # setup_script_content += f'pip install {req}\n'
    # setup_script_content += f'pip install deepspeed || conda install deepspeed -y\n' # hotwire cus no cuda on mac 
    # setup_script_content += f'pip install transformers git+https://github.com/huggingface/transformers.git@ab37b801b14d8b9c3186548e6e118aff623e6aa1 || conda install transformers git+https://github.com/huggingface/transformers.git@ab37b801b14d8b9c3186548e6e118aff623e6aa1 -y\n'
    setup_script_content += f'{on_start_cmd}\n'
    

    return setup_script_content

# def create_choline_yaml(image_name, direct_copy_locations, start_cmd, gpu_name, disk_space, wndb_key, cpu_ram):
#     choline_yaml = {
#         'image': image_name,
#         'upload_locations': direct_copy_locations,
#         'onStart': start_cmd,
#         'local_cuda_version': get_local_cuda_version(),
#         'python_version': get_python_version(),
#         'conda_version': get_conda_version(),
#         'hardware_filters': {'gpu_name': gpu_name, 'disk_space': disk_space, 'cpu_ram': cpu_ram},
#     }
#     choline_yaml_path = Path.cwd() / 'choline.yaml'

#     with open(choline_yaml_path, 'w') as f:
#         yaml.dump(choline_yaml, f, default_flow_style=False, indent=2)
#         f.write("setup_script: |\n")
#         setup_script_content = create_setup_script(wndb_key, start_cmd)
#         setup_script_content = '  ' + setup_script_content.replace('\n', '\n  ')
#         f.write(setup_script_content)

from pathlib import Path
import yaml

def literal_str(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='')

yaml.add_representer(str, literal_str)

def create_choline_yaml(image_name, direct_copy_locations, start_cmd, gpu_name, disk_space, wndb_key, cpu_ram, ignore_list):
    choline_yaml = {
        'image': image_name,
        'upload_locations': direct_copy_locations,
        'onStart': start_cmd,
        'local_cuda_version': get_local_cuda_version(),
        'python_version': get_python_version(),
        'conda_version': get_conda_version(),
        'hardware_filters': {'gpu_name': gpu_name, 'disk_space': disk_space, 'cpu_ram': cpu_ram},
        'ignore': ignore_list
    }
    
    choline_yaml_path = Path.cwd() / 'choline.yaml'

    with open(choline_yaml_path, 'w') as f:
        yaml.dump(choline_yaml, f, default_flow_style=False, indent=2)
        
        f.write("setup_script: |\n")
        setup_script_content = create_setup_script(wndb_key, start_cmd)
        setup_script_content = '  ' + setup_script_content.replace('\n', '\n  ')
        f.write(setup_script_content)
        
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
        'RTX_A6000'
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



def ask_for_cpu_ram():
    disk_space = input("Enter the amount of CPU RAM needed (in GB): ")
    return f">{disk_space}"



def ask_for_disk_space():
    disk_space = input("Enter the amount of disk space needed (in GB): ")
    return f">{disk_space}"


def ask_for_wandb_api_key():
    wandb_api_key = input("Enter your wandb API key: ")
    return wandb_api_key

import os
import fnmatch

def suggest_files_to_ignore(upload_locations):
    common_ignore_files = [
        '.DS_Store', '__pycache__', '*.pyc', '*.pyo', '*.egg-info/', 'env/', 
        '.ipynb_checkpoints/', '.git/', '*.swp', '*.swo', '.vscode/', '*.bak',
        '*.csv', '*.log', '*.tmp', '*.json', 'node_modules/', '.env', 'venv/',
        '.gitignore', '.dockerignore', '*.gz', '*.md', '*.rst'
    ]
    files_to_ignore = []
    ignore_dict = {}
    ignore_list = []
    pattern_count = {}
    
    for location in upload_locations:
        for root, _, files in os.walk(location):
            for file in files:
                for pattern in common_ignore_files:
                    if fnmatch.fnmatch(file, pattern):
                        full_path = os.path.join(root, file)
                        files_to_ignore.append(full_path)
                        pattern_count[pattern] = pattern_count.get(pattern, 0) + 1
    
    if files_to_ignore:
        print("Suggested files to ignore:")
        counter = 1
        for pattern, count in pattern_count.items():
            print(f"{counter}. {pattern} (all files with {pattern} pattern: {count} file(s))")
            ignore_dict[counter] = pattern
            counter += 1

        print("Individual files:")
        for idx, file in enumerate(files_to_ignore, counter):
            print(f"{idx}. {file}")
            ignore_dict[idx] = file

        selected_indices = input("Enter the numbers corresponding to the files or file types you want to ignore, or type 'all' (comma-separated): ")

        if selected_indices.strip().lower() == 'all':
            ignore_list = list(pattern_count.keys())
            print(f"Added all patterns to the ignore list: {ignore_list}")
        else:
            selected_indices = [int(idx.strip()) for idx in selected_indices.split(',') if idx.strip().isdigit()]
            for idx in selected_indices:
                if idx in ignore_dict:
                    print(f"Added {ignore_dict[idx]} to the ignore list.")
                    ignore_list.append(ignore_dict[idx])
                else:
                    print(f"Invalid index {idx}. Skipping.")
    
    return ignore_list





def init_command():
    image = ask_for_image_choice()
    _, copy_locations = create_upload_dirs()
    ignore_list = suggest_files_to_ignore(copy_locations)
    start_cmd = create_run_cmd()
    gpu_filters = ask_for_gpu_choice()
    disk_space = ask_for_disk_space()
    wdb_key = ask_for_wandb_api_key()
    cpu_ram = ask_for_cpu_ram()
    # create_choline_json(image, removed, copy_locations, start_cmd, gpu_filters, disk_space)
    create_choline_yaml(image, copy_locations, start_cmd, gpu_filters, disk_space, wndb_key=wdb_key, cpu_ram=cpu_ram, ignore_list=ignore_list)


def run():
    init_command()










# def create_setup_script():
#     python_version = get_python_version()
#     setup_script_content = f'''#!/bin/bash
#     # Download Miniconda installer
#     wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
#     # Install Miniconda
#     bash miniconda.sh -b -p $HOME/miniconda
#     # Initialize conda
#     source $HOME/miniconda/bin/activate
#     conda init
#     # Create environment
#     conda create --name choline python={python_version} -y
#     # Activate environment
#     conda activate choline
#     '''
#     requirements = get_requirements_list()
#     for req in requirements:
#         setup_script_content += f'conda install {req} -y || pip install {req}\n'
#     choline_setup_path = Path.cwd() / ".choline" / "choline_setup.sh"
#     with open(choline_setup_path, 'w') as f:
#         f.write(setup_script_content)




# def create_choline_yaml(image_name, direct_copy_locations, start_cmd, gpu_name, disk_space):
#     choline_yaml = {
#         "image": image_name,
#         "upload_locations": direct_copy_locations,
#         "onStart": start_cmd,
#         "local_cuda_version": get_local_cuda_version(),
#         "python_version": get_python_version(),
#         "setup_script": # todo 
#         "conda_version": get_conda_version(),
#         "hardware_filters": {"gpu_name": gpu_name, "disk_space": disk_space}
#     }

#     choline_yaml_path = Path.cwd() / "choline.yaml"
#     with open(choline_yaml_path, 'w') as f:
#         yaml.dump(choline_yaml, f, default_flow_style=False, indent=4)


# def create_setup_script():
#     # Create .choline directory if it doesn't exist
#     choline_dir = os.path.join(os.getcwd(), ".choline")
#     if not os.path.exists(choline_dir):
#         os.makedirs(choline_dir)


#     python_version = get_python_version()
#     setup_script_content = f'''#!/bin/bash
#     # Download Miniconda installer
#     wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
#     # Install Miniconda
#     bash miniconda.sh -b -p $HOME/miniconda
#     # Initialize conda
#     source $HOME/miniconda/bin/activate
#     conda init
#     # Create environment
#     conda create --name choline python={python_version} -y
#     # Activate environment
#     conda activate choline
#     '''
#     requirements = get_requirements_list()
#     for req in requirements:
#         setup_script_content += f'conda install {req} -y || pip install {req}\n'
#     choline_setup_path = Path.cwd() / ".choline" / "choline_setup.sh"
#     with open(choline_setup_path, 'w') as f:
#         f.write(setup_script_content)
#     return str(choline_setup_path)

# def create_choline_yaml(image_name, direct_copy_locations, start_cmd, gpu_name, disk_space):
#     setup_script_path = create_setup_script()
#     choline_yaml = {
#         "image": image_name,
#         "upload_locations": direct_copy_locations,
#         "onStart": start_cmd,
#         "local_cuda_version": get_local_cuda_version(),
#         "python_version": get_python_version(),
#         "setup_script": setup_script_path,
#         "conda_version": get_conda_version(),
#         "hardware_filters": {"gpu_name": gpu_name, "disk_space": disk_space}
#     }

#     choline_yaml_path = Path.cwd() / "choline.yaml"
#     with open(choline_yaml_path, 'w') as f:
#         yaml.dump(choline_yaml, f, default_flow_style=False, indent=4)

# def create_setup_script():
#     python_version = get_python_version()
#     setup_script_content = f'''#!/bin/bash
# # Download Miniconda installer
# wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
# # Install Miniconda
# bash miniconda.sh -b -p $HOME/miniconda
# # Initialize conda
# source $HOME/miniconda/bin/activate
# conda init
# # Create environment
# conda create --name choline python={python_version} -y
# # Activate environment
# conda activate choline
# '''
#     requirements = get_requirements_list()
#     for req in requirements:
#         setup_script_content += f'conda install {req} -y || pip install {req}'
#     return setup_script_content

# def create_choline_yaml(image_name, direct_copy_locations, start_cmd, gpu_name, disk_space, wndb_key):
#     choline_yaml = {
#         'wandb_key': wndb_key,
#         'image': image_name,
#         'upload_locations': direct_copy_locations,
#         'onStart': start_cmd,
#         'local_cuda_version': get_local_cuda_version(),
#         'python_version': get_python_version(),
#         'conda_version': get_conda_version(),
#         'hardware_filters': {'gpu_name': gpu_name, 'disk_space': disk_space},
#     }
#     choline_yaml_path = Path.cwd() / 'choline.yaml'

#     with open(choline_yaml_path, 'w') as f:
#         yaml.dump(choline_yaml, f, default_flow_style=False, indent=2)
#         f.write("setup_script: |\n")
#         setup_script_content = create_setup_script()
#         setup_script_content = '  ' + setup_script_content.replace('\n', '\n  ')
#         f.write(setup_script_content)

# def create_setup_script(wndb_key, on_start_cmd):
#     python_version = get_python_version()
#     setup_script_content = f'''#!/bin/bash
# # Download Miniconda installer
# wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
# # Install Miniconda
# bash miniconda.sh -b -p $HOME/miniconda
# # Initialize conda
# . $HOME/miniconda/bin/activate
# conda init
# # Create environment
# conda create --name choline python={python_version} -y
# # Activate environment
# conda activate choline
# # Install vim
# sudo apt install vim -y
# # Set Wandb API key without user interaction
# export WANDB_API_KEY={wndb_key}
# '''

#     requirements = get_requirements_list()
#     for req in requirements:
#         setup_script_content += f'pip install {req} || conda install {req} -y\n'
#     setup_script_content += f'pip install deepspeed || conda install deepspeed -y\n' # hotwire cus no cuda on mac 
#     setup_script_content += f'pip install transformers git+https://github.com/huggingface/transformers.git@ab37b801b14d8b9c3186548e6e118aff623e6aa1 || conda install transformers git+https://github.com/huggingface/transformers.git@ab37b801b14d8b9c3186548e6e118aff623e6aa1 -y\n'
#     setup_script_content += f'{on_start_cmd}\n'
    

#     return setup_script_content

