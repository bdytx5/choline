
import argparse
import subprocess
import os
import sys
import json 
from pathlib import Path

import yaml 
import shutil
from datetime import datetime



from pathlib import Path
import yaml


import os
import fnmatch

CREDS_FILE = Path.home() / ".choline" / "creds.yaml"

def ensure_creds_file():
    if not CREDS_FILE.exists():
        print(f"Creating {CREDS_FILE}...")
        CREDS_FILE.parent.mkdir(parents=True, exist_ok=True)
        username = input("Enter your GitHub username: ")
        github_token = input("Enter your GitHub token: ")
        creds = {
            'username': username,
            'github_token': github_token
        }
        with open(CREDS_FILE, 'w') as f:
            yaml.dump(creds, f)
        print(f"{CREDS_FILE} created with provided values.")
    else:
        with open(CREDS_FILE, 'r') as f:
            creds = yaml.safe_load(f)
        
        if 'username' not in creds or 'github_token' not in creds:
            print(f"{CREDS_FILE} is missing some values.")
            if 'username' not in creds:
                creds['username'] = input("Enter your GitHub username: ")
            if 'github_token' not in creds:
                creds['github_token'] = input("Enter your GitHub token: ")
            
            with open(CREDS_FILE, 'w') as f:
                yaml.dump(creds, f)
            print(f"{CREDS_FILE} updated with provided values.")



import requests
from pathlib import Path
import yaml
# def ask_create_repo():
#     creds_file = Path.home() / ".choline" / "creds.yaml"
#     if not creds_file.exists():
#         raise FileNotFoundError("Credentials file not found. Please create ~/.choline/creds.yaml with the necessary Git credentials.")

#     with open(creds_file, 'r') as f:
#         creds = yaml.safe_load(f)

#     if 'username' not in creds or 'github_token' not in creds:
#         raise ValueError("Credentials file is missing necessary Git credentials. Please add 'username' and 'github_token' to ~/.choline/creds.yaml.")

#     git_username = creds['username']
#     github_token = creds['github_token']
    
#     # Check if any remote repository is set
#     try:
#         result = subprocess.run(["git", "config", "--get", "remote.origin.url"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         remote_url = result.stdout.decode().strip()
#         if remote_url:
#             print(f"Remote repository is already set: {remote_url}")
#             return True
#         else:
#             print("No remote repository is set.")
#     except subprocess.CalledProcessError:
#         print("This directory is not a Git repository. You need to initialize a Git repository and set a remote URL.")
    
#     repo_name = input("Enter the name of the repository you want to create: ")
#     create_choice = input("Do you want to create a new repository? Enter 'p' for private, 'b' for public, or press Enter to exit: ").lower()
    
#     if create_choice == 'p':
#         repo_private = True
#     elif create_choice == 'b':
#         repo_private = False
#     else:
#         print("Exiting without creating a repository.")
#         return False

#     create_repo_payload = {
#         "name": repo_name,
#         "private": repo_private
#     }
    
#     create_response = requests.post(f"https://api.github.com/user/repos", auth=(git_username, github_token), json=create_repo_payload)
    
#     if create_response.status_code == 201:
#         print(f"Repository '{repo_name}' created successfully.")
#         return True
#     else:
#         print(f"Failed to create repository. Status code: {create_response.status_code}")
#         print(create_response.json())
#         return False

import subprocess
import requests
import yaml
import os
from pathlib import Path

def ask_create_repo():
    creds_file = Path.home() / ".choline" / "creds.yaml"
    if not creds_file.exists():
        raise FileNotFoundError("Credentials file not found. Please create ~/.choline/creds.yaml with the necessary Git credentials.")

    with open(creds_file, 'r') as f:
        creds = yaml.safe_load(f)

    if 'username' not in creds or 'github_token' not in creds:
        raise ValueError("Credentials file is missing necessary Git credentials. Please add 'username' and 'github_token' to ~/.choline/creds.yaml.")

    git_username = creds['username']
    github_token = creds['github_token']
    
    # Check if any remote repository is set
    try:
        result = subprocess.run(["git", "config", "--get", "remote.origin.url"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        remote_url = result.stdout.decode().strip()
        if remote_url:
            print(f"Remote repository is already set: {remote_url}")
            return True
        else:
            print("No remote repository is set.")
    except subprocess.CalledProcessError:
        print("This directory is not a Git repository. You need to initialize a Git repository and set a remote URL.")
    
    repo_name = input("Enter the name of the repository you want to create: ")
    create_choice = input("Do you want to create a new repository? Enter 'p' for private, 'b' for public, or press Enter to exit: ").lower()
    
    if create_choice == 'p':
        repo_private = True
    elif create_choice == 'b':
        repo_private = False
    else:
        print("Exiting without creating a repository.")
        return False

    create_repo_payload = {
        "name": repo_name,
        "private": repo_private
    }
    
    create_response = requests.post(f"https://api.github.com/user/repos", auth=(git_username, github_token), json=create_repo_payload)
    
    if create_response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
        
        # Initialize git repository if not already initialized
        subprocess.run(["git", "init"], check=True)
        
        # Add .gitignore if the user wants to
        input("If you would like to add a .gitignore file before pushing, please do it now. Press Enter to continue when ready.")
        
        # Create a .gitignore file
        with open('.gitignore', 'a') as f:
            f.write("choline.yaml\n")
            f.write(".choline/\n")
        
        # Add all files except those in .gitignore
        subprocess.run(["git", "add", "."], check=True)
        
        # Commit the changes
        subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
        
        # Add the remote repository
        remote_url = f"https://{git_username}:{github_token}@github.com/{git_username}/{repo_name}.git"
        subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
        
        # Push the changes
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        
        return True
    else:
        print(f"Failed to create repository. Status code: {create_response.status_code}")
        print(create_response.json())
        return False
    
    # def ask_create_repo():
#     creds_file = Path.home() / ".choline" / "creds.yaml"
#     if not creds_file.exists():
#         raise FileNotFoundError("Credentials file not found. Please create ~/.choline/creds.yaml with the necessary Git credentials.")

#     with open(creds_file, 'r') as f:
#         creds = yaml.safe_load(f)

#     if 'username' not in creds or 'github_token' not in creds:
#         raise ValueError("Credentials file is missing necessary Git credentials. Please add 'username' and 'github_token' to ~/.choline/creds.yaml.")

#     git_username = creds['username']
#     github_token = creds['github_token']
    
#     repo_name = input("Enter the name of the repository you want to create or check: ")
#     repo_url = f"https://api.github.com/repos/{git_username}/{repo_name}"
    
#     response = requests.get(repo_url, auth=(git_username, github_token))
    
#     if response.status_code == 200:
#         print(f"The repository '{repo_name}' already exists.")
#     else:
#         print(f"The repository '{repo_name}' does not exist.")
#         create_choice = input("Do you want to create a new repository? Enter 'p' for private, 'b' for public, or press Enter to exit: ").lower()
        
#         if create_choice == 'p':
#             repo_private = True
#         elif create_choice == 'b':
#             repo_private = False
#         else:
#             print("Exiting without creating a repository.")
#             return

#         create_repo_payload = {
#             "name": repo_name,
#             "private": repo_private
#         }
        
#         create_response = requests.post(f"https://api.github.com/user/repos", auth=(git_username, github_token), json=create_repo_payload)
        
#         if create_response.status_code == 201:
#             print(f"Repository '{repo_name}' created successfully.")
#         else:
#             print(f"Failed to create repository. Status code: {create_response.status_code}")
#             print(create_response.json())

# # Example usage





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


# def create_setup_script(wndb_key, hf_key, on_start_cmd):
#     setup_script_content = f'''#!/bin/bash
# # Download Miniconda installer
# # wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
# # Install Miniconda
# # bash miniconda.sh -b -p $HOME/miniconda
# # Initialize conda
# # . $HOME/miniconda/bin/activate
# # conda init
# # Create environment
# # conda create --name choline python=3.10 -y
# # Activate environment
# # conda activate choline
# # Install vim
# export cholineremote=true
# sudo apt upgrade
# sudo apt install vim -y
# sudo apt install python3.9
# sudo apt install python-is-python3 -y
# sudo apt install python3-pip -y
# # Set Wandb API key without user interaction
# export WANDB_API_KEY={wndb_key}
# pip install huggingface || pip3 install huggingface -y\n
# # Log in to Hugging Face CLI
# echo '{hf_key}' | huggingface-cli login --stdin
# echo 'n' | huggingface-cli whoami
# '''

#     requirements = get_requirements_list()
#     for req in requirements:
        
#         if len(req) <= 1:
#             continue
#         if '@ file:' in req or 'pyobjc' in req:
#             print(f"Skipping {req}")
#             continue

#         setup_script_content += f'pip install {req} || pip3 install {req} -y\n'
#     setup_script_content += f'{on_start_cmd}\n'

#     return setup_script_content

import yaml
from pathlib import Path
import subprocess

def get_git_remote_url():
    try:
        subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = subprocess.run(["git", "config", "--get", "remote.origin.url"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        remote_url = result.stdout.decode().strip()
        if remote_url:
            return remote_url
        else:
            print("No remote URL is set for this Git repository. You need to set one.")
            
            return None
    except subprocess.CalledProcessError:
        print("This directory is not a Git repository. You need to initialize a Git repository and set a remote URL.")
        return None

def create_setup_script(wndb_key, hf_key, on_start_cmd):
    creds_file = Path.home() / ".choline" / "creds.yaml"
    if not creds_file.exists():
        raise FileNotFoundError("Credentials file not found. Please create ~/.choline/creds.yaml with the necessary Git credentials.")
    
    with open(creds_file, 'r') as f:
        creds = yaml.safe_load(f)
    
    if 'username' not in creds or 'github_token' not in creds:
        raise ValueError("Credentials file is missing necessary Git credentials. Please add 'username' and 'github_token' to ~/.choline/creds.yaml.")
    
    git_username = creds['username']
    github_token = creds['github_token']
    
    remote_url = get_git_remote_url()
    if remote_url is None:
        raise ValueError("Git remote URL is not set. Please initialize a Git repository and set a remote URL.")

    setup_script_content = f'''#!/bin/bash
# Ensure Git is installed
sudo apt update
sudo apt install git -y

# Download Miniconda installer
# wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
# Install Miniconda
# bash miniconda.sh -b -p $HOME/miniconda
# Initialize conda
# . $HOME/miniconda/bin/activate
# conda init
# Create environment
# conda create --name choline python=3.10 -y
# Activate environment
# conda activate choline
# Install vim
export cholineremote=true
sudo apt upgrade
sudo apt install vim -y
sudo apt install python3.9
sudo apt install python-is-python3 -y
sudo apt install python3-pip -y
# Set Wandb API key without user interaction
export WANDB_API_KEY={wndb_key}
pip install huggingface || pip3 install huggingface -y
# Log in to Hugging Face CLI
echo '{hf_key}' | huggingface-cli login --stdin
echo 'n' | huggingface-cli whoami

# Set Git credentials
git config --global user.name "{git_username}"
git config --global user.email "{git_username}@users.noreply.github.com"
git config credential.helper store
echo "https://{git_username}:{github_token}@github.com" > ~/.git-credentials

# Clone the repository
git clone {remote_url} repo
cd repo
'''

    requirements = get_requirements_list()
    for req in requirements:
        if len(req) <= 1:
            continue
        if '@ file:' in req or 'pyobjc' in req:
            print(f"Skipping {req}")
            continue
        setup_script_content += f'pip install {req} || pip3 install {req} -y\n'
    
    setup_script_content += "echo '0' > ~/.choline/setup_complete.txt\n" # setup is now complete 

    # setup_script_content += f'{on_start_cmd}\n'
    setup_script_content += f'''{on_start_cmd}
    if [ $? -ne 0 ]; then
        echo "Setup command failed with exit code $?" > ~/.choline/failed.txt
    fi
    ''' # track failures 

    return setup_script_content

# Example call to the function
# setup_script = create_setup_script('your_wandb_key', 'your_hf_key', 'your_start_cmd')
# print(setup_script)


def literal_str(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='')

yaml.add_representer(str, literal_str)

def create_choline_yaml(image_name, direct_copy_locations, start_cmd, gpu_name, disk_space, wndb_key, cpu_ram, ignore_list, num_gpus, hf_key):
    choline_yaml = {
        'image': image_name,
        'upload_locations': direct_copy_locations,
        'onStart': start_cmd,
        'local_cuda_version': get_local_cuda_version(),
        'python_version': get_python_version(),
        'conda_version': get_conda_version(),
        'hardware_filters': {'gpu_name': gpu_name, 'disk_space': disk_space, 'cpu_ram': cpu_ram},
        'ignore': ignore_list, 
        'num_gpus': num_gpus
    }
    
    choline_yaml_path = Path.cwd() / 'choline.yaml'

    with open(choline_yaml_path, 'w') as f:
        yaml.dump(choline_yaml, f, default_flow_style=False, indent=2)
        
        f.write("setup_script: |\n")
        setup_script_content = create_setup_script(wndb_key, hf_key, start_cmd)
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

def ask_for_num_gpus():
    while True:
        try:
            gpus = input("Enter the number of GPU's needed (1-128): ")
            gpus_int = int(gpus)  # Convert the input to an integer
            if 1 <= gpus_int <= 128:
                return f"{gpus_int}"
            else:
                print("Please enter a number between 1 and 128.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


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




# def init_command():
#     image = ask_for_image_choice()
#     _, copy_locations = create_upload_dirs()
#     ignore_list = suggest_files_to_ignore(copy_locations)
#     start_cmd = create_run_cmd()
#     gpu_filters = ask_for_gpu_choice()
#     disk_space = ask_for_disk_space()

#     wdb_key = os.getenv("WANDB_API_KEY")
#     if wdb_key is None:
#         wdb_key = input("Enter your Weights & Biases API key: ")
#     else:
#         print("Using Weights & Biases API key from environment variable.")

#     hf_key = os.getenv("HUGGINGFACE_API_KEY")
#     if hf_key is None:
#         hf_key = input("Enter your Hugging Face API key: ")
#     else:
#         print("Using Hugging Face API key from environment variable.")

#     # Determine the shell configuration file based on the user's shell
#     shell = os.environ.get('SHELL', '')
#     if 'zsh' in shell:
#         config_file = '~/.zshrc'
#     else:
#         config_file = '~/.bashrc'

#     # Check if the API keys are already present in the shell configuration file
#     with open(os.path.expanduser(config_file), 'r') as f:
#         config_content = f.read()

#     # Echo the API keys to the shell configuration file if they are not already present
#     if f'export WANDB_API_KEY="{wdb_key}"' not in config_content:
#         with open(os.path.expanduser(config_file), 'a') as f:
#             f.write(f'\nexport WANDB_API_KEY="{wdb_key}"\n')

#     if f'export HUGGINGFACE_API_KEY="{hf_key}"' not in config_content:
#         with open(os.path.expanduser(config_file), 'a') as f:
#             f.write(f'export HUGGINGFACE_API_KEY="{hf_key}"\n')

#     # Source the shell configuration file
#     os.system(f'source {config_file}')

#     cpu_ram = ask_for_cpu_ram()
#     num_gpus = ask_for_num_gpus()

#     create_choline_yaml(
#         image,
#         copy_locations,
#         start_cmd,
#         gpu_filters,
#         disk_space,
#         wndb_key=wdb_key,
#         hf_key=hf_key,
#         cpu_ram=cpu_ram,
#         ignore_list=ignore_list,
#         num_gpus=num_gpus
#     )


# def init_command():
#     ensure_creds_file()
#     image = ask_for_image_choice()
#     _, copy_locations = create_upload_dirs()
#     ignore_list = suggest_files_to_ignore(copy_locations)
#     start_cmd = create_run_cmd()
#     gpu_filters = ask_for_gpu_choice()
#     disk_space = ask_for_disk_space()

#     creds_file = Path.home() / ".choline" / "creds.yaml"
#     if creds_file.exists():
#         with open(creds_file, 'r') as f:
#             creds = yaml.safe_load(f)
#     else:
#         creds = {}

#     if 'WANDB_API_KEY' in creds:
#         wdb_key = creds['WANDB_API_KEY']
#         print("Using Weights & Biases API key from creds.yaml.")
#     else:
#         wdb_key = input("Enter your Weights & Biases API key: ")
#         creds['WANDB_API_KEY'] = wdb_key

#     if 'HUGGINGFACE_API_KEY' in creds:
#         hf_key = creds['HUGGINGFACE_API_KEY']
#         print("Using Hugging Face API key from creds.yaml.")
#     else:
#         hf_key = input("Enter your Hugging Face API key: ")
#         creds['HUGGINGFACE_API_KEY'] = hf_key

#     with open(creds_file, 'w') as f:
#         yaml.dump(creds, f)

#     cpu_ram = ask_for_cpu_ram()
#     num_gpus = ask_for_num_gpus()

#     create_choline_yaml(
#         image,
#         copy_locations,
#         start_cmd,
#         gpu_filters,
#         disk_space,
#         wndb_key=wdb_key,
#         hf_key=hf_key,
#         cpu_ram=cpu_ram,
#         ignore_list=ignore_list,
#         num_gpus=num_gpus
#     )



def init_command():
    ensure_creds_file()
    
    # Only proceed if ask_create_repo returns True (repository created or already exists)
    if not ask_create_repo():
        print("Repository creation unsuccessful.")
        return

    image = ask_for_image_choice()
    _, copy_locations = create_upload_dirs()
    ignore_list = suggest_files_to_ignore(copy_locations)
    start_cmd = create_run_cmd()
    gpu_filters = ask_for_gpu_choice()
    disk_space = ask_for_disk_space()

    creds_file = Path.home() / ".choline" / "creds.yaml"
    if creds_file.exists():
        with open(creds_file, 'r') as f:
            creds = yaml.safe_load(f)
    else:
        creds = {}

    if 'WANDB_API_KEY' in creds:
        wdb_key = creds['WANDB_API_KEY']
        print("Using Weights & Biases API key from creds.yaml.")
    else:
        wdb_key = input("Enter your Weights & Biases API key: ")
        creds['WANDB_API_KEY'] = wdb_key

    if 'HUGGINGFACE_API_KEY' in creds:
        hf_key = creds['HUGGINGFACE_API_KEY']
        print("Using Hugging Face API key from creds.yaml.")
    else:
        hf_key = input("Enter your Hugging Face API key: ")
        creds['HUGGINGFACE_API_KEY'] = hf_key

    with open(creds_file, 'w') as f:
        yaml.dump(creds, f)

    cpu_ram = ask_for_cpu_ram()
    num_gpus = ask_for_num_gpus()

    create_choline_yaml(
        image,
        copy_locations,
        start_cmd,
        gpu_filters,
        disk_space,
        wndb_key=wdb_key,
        hf_key=hf_key,
        cpu_ram=cpu_ram,
        ignore_list=ignore_list,
        num_gpus=num_gpus
    )



def run():
    init_command()


