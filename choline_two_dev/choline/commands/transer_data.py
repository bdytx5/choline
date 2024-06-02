



import subprocess
import os
import json
import time
import argparse
import platform
import paramiko
from scp import SCPClient, SCPException
from fnmatch import fnmatch
import traceback
import yaml 
import re
import uuid
import requests


print("Exception traceback:")
traceback.print_exc()

import yaml

def get_choline_yaml_data():
    with open('choline.yaml', 'r') as f:
        data = yaml.safe_load(f)
    return data



def send_alert(message):
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system(f'echo "{message}" | wall')


def store_file_timestamp(file_path, username, host, port, choline_dir=".choline"):
    timestamp_json_filename = f"file_timestamps_{username}_{host}_{port}.json"
    timestamp_json_path = os.path.join(choline_dir, timestamp_json_filename)
    last_modified_time = os.path.getmtime(file_path)
    
    if os.path.exists(timestamp_json_path):
        with open(timestamp_json_path, "r") as f:
            file_data = json.load(f)
    else:
        file_data = {}
    
    file_data[file_path] = last_modified_time
    
    with open(timestamp_json_path, "w") as f:
        json.dump(file_data, f)


def should_ignore(path, ignore_patterns):
    for pattern in ignore_patterns:
        if fnmatch(path, pattern):
            return True
    return False

# def get_ssh_details(ssh_address):
#     username, rest = ssh_address.split('@')
#     host, port = rest.split(':')
#     return username, host, port


def get_ssh_details(ssh_address):
    username, rest = ssh_address.split('@')
    if ':' in rest:
        host, port = rest.split(':')
    else:
        host = rest
        port = None  # Set a default port here if you like, or keep it None
    return username, host, port



def ssh_copy_directory_full_path(scp, ssh, local_path, remote_base_path, ignore_patterns, username, host, port):
    
    for root, dirs, files in os.walk(local_path):
        for file_name in files:
            local_file = os.path.join(root, file_name)
            
            if should_ignore(local_file, ignore_patterns):
                continue
            
            # Store the file's timestamp before uploading
            store_file_timestamp(local_file, username, host, port)
            
            remote_file = remote_base_path + local_file
            remote_dir = os.path.dirname(remote_file)            

            stdin, stdout, stderr = ssh.exec_command(f"mkdir -p {remote_dir}")
            stdout.read()
            print("local = {} remote destin = {}".format(local_file, remote_file))
            try:
                scp.put(local_file, remote_file)
            except SCPException as e:
                print(f"SCP Exception for {remote_file}: {str(e)}")
                print("Error details: ", stderr.read().decode())




def ssh_copy_directory_local_path(scp, ssh, local_path, remote_base_path, ignore_patterns, username, host, port):
    folder_name = os.path.basename(local_path)  # Extract only the folder name
    remote_base_path = os.path.join(remote_base_path, folder_name)  # Append folder name to the remote base path
    
    for root, dirs, files in os.walk(local_path):
        for file_name in files:
            local_file = os.path.join(root, file_name)
            
            if should_ignore(local_file, ignore_patterns):
                continue
            
            # Store the file's timestamp before uploading
            store_file_timestamp(local_file, username, host, port)
            
            # Calculate the relative path
            relative_path = os.path.relpath(local_file, local_path)
            
            # Create the full remote file path
            remote_file = os.path.join(remote_base_path, relative_path)
            remote_dir = os.path.dirname(remote_file)

            stdin, stdout, stderr = ssh.exec_command(f"mkdir -p {remote_dir}")
            stdout.read()
            print("local = {} remote destin = {}".format(local_file, remote_file))
            try:
                scp.put(local_file, remote_file)
            except SCPException as e:
                print(f"SCP Exception for {remote_file}: {str(e)}")
                print("Error details: ", stderr.read().decode())



def ssh_copy_file_or_dir(username, host, port, src, dest, ignore_patterns):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    mykey = paramiko.RSAKey(filename='/Users/brettyoung/.ssh/new_rsa_key')

    client.connect(host, username=username, pkey=mykey)
    with SCPClient(client.get_transport()) as scp:
        if os.path.isdir(src):
            print(scp, client, src, dest, ignore_patterns, username, host,port)
            ssh_copy_directory_full_path(scp, client, src, dest, ignore_patterns, username=username, host=host, port=port)
        else:
            # Create remote directories if they don't exist
            # remote_file = os.path.join(dest, src)
            remote_file = dest + src
            print("REMOTE: {}".format(remote_file))
            remote_dir = os.path.dirname(remote_file)                        
            print("REMOTE: {}".format(remote_dir))
            stdin, stdout, stderr = client.exec_command(f"mkdir -p {remote_dir}")
            print(stderr.read().decode())
            print(stdout.read().decode())
            store_file_timestamp(src, username, host, port)
            remote_file = os.path.join(dest, src) # using full paths            
            try:
                scp.put(src, remote_dir)
            except SCPException as e:
                print(f"SCP Exception for {remote_file}: {str(e)}")
                print("Error details: ", stderr.read().decode())

            
    client.close()


def send_choline_setup(vastai_id, max_retries=100):
    choline_data = get_choline_yaml_data()
    setup_script = choline_data.get('setup_script', '')

    local_path = os.path.join(os.getcwd(), '.choline')
    if not os.path.exists(local_path):
        os.makedirs(local_path)

    setup_script_path = os.path.join(local_path, 'choline_setup.sh')

    with open(setup_script_path, 'w') as f:
        f.write(setup_script)

    username, host, port = get_ssh_details(vastai_id)
    remote_path = '/root/choline'
    retries = 0
    while retries < max_retries:
        try:
            ssh_copy_file_or_dir(username, host, port, local_path, remote_path)
            print("Sent setup script to instance.")
            break
        except Exception as e:
            print(f"Error to send choline setup: {e}. Waiting 20 seconds before retrying.")
            time.sleep(20)
            retries += 1


def send_choline_dir(username, host, port, src, dest, ignore_patterns, max_retries=30):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    mykey = paramiko.RSAKey(filename='/Users/brettyoung/.ssh/new_rsa_key')

    client.connect(host, username=username, pkey=mykey)

    retries = 0
    while retries < max_retries:
        with SCPClient(client.get_transport()) as scp:
            if os.path.isdir(src):
                print(scp, client, src, dest, ignore_patterns, username, host,port)
                try: 
                    ssh_copy_directory_local_path(scp, client, src, dest, ignore_patterns, username=username, host=host, port=port)            
                    client.close()
                    break
                except Exception as e: 
                    client.close()
                    print(str(e))
                    continue
        retries+=1 

# Add this function to send data to the Flask API
def set_upload_complete_in_db(key, sshStorageAddress, max_hrly_hardware_cost, image):
    yml = get_choline_yaml_data()
    hardware = yml['hardware_filters']
    payload = {
        "key": key,
        "hardware_filters": hardware,
        "sshStorageAddress": sshStorageAddress,
        "max_hrly_hardware_cost": max_hrly_hardware_cost,
        "image": image
    }
    requests.post("http://34.28.218.185:8080/cholineCompletedUploads", json=payload)





# def read_setup_from_choline_yaml(instance_base_pth):
#     choline_data = get_choline_yaml_data()
    
#     setup_script = choline_data.get('setup_script', '')
#     cwd = os.getcwd()

#     setup_script_path = os.path.join(cwd, ".choline", "choline_setup.sh")

#     # Save the script to a file
#     with open(setup_script_path, "w") as f:
#         f.write(setup_script)

#     return setup_script_path


### added the base path to the run command 
import os

def read_setup_from_choline_yaml_and_adjust_run_pth(instance_base_pth):
    choline_data = get_choline_yaml_data()
    
    setup_script = choline_data.get('setup_script', '')
    lines = setup_script.split("\n")
    modified_lines = []

    for line in lines:
        if line.startswith("python ") or line.startswith("python3 "):
            parts = line.split(" ", 1)
            new_script_path = os.path.join(instance_base_pth, parts[1].lstrip("/"))
            line = f"{parts[0]} {new_script_path}"
        modified_lines.append(line)

    modified_setup_script = "\n".join(modified_lines)

    cwd = os.getcwd()
    setup_script_path = os.path.join(cwd, ".choline", "choline_setup.sh")

    # Save the modified script to a file
    with open(setup_script_path, "w") as f:
        f.write(modified_setup_script)

    return setup_script_path



def main(ssh_address, max_checks, max_cost):
    remote_base_path = '/root'
    read_setup_from_choline_yaml_and_adjust_run_pth(remote_base_path)
    choline_data = get_choline_yaml_data()
    ignore_patterns = choline_data.get('ignore', [])
    upload_locations = choline_data.get('upload_locations', [])
    image = choline_data.get('image')
    key = str(uuid.uuid4())
    username, host, port = get_ssh_details(ssh_address=ssh_address)
    for location in upload_locations:
        try:
            # local_path = os.path.join(os.getcwd(), location)
            print(username, host, port,  location, '/home/byyoung3/{}'.format(key), ignore_patterns)
            # ssh_copy_file_or_dir(ssh_address, local_path, '/home/brett/{}'.format(key), ignore_patterns)
            ssh_copy_file_or_dir(username, host, port,  location, '/home/byyoung3/{}'.format(key), ignore_patterns)

            print(f"Sent location {location}")
        except Exception as e:
            print(f"Failed to send {location}: {e}")
            return 
    ### send key to firebase at /completedUploads/key/-> and set the 
    choline_dir = os.path.join(os.getcwd(), '.choline')
    send_choline_dir(username, host, port,  choline_dir, '/home/byyoung3/{}'.format(key), ignore_patterns)
    # ssh_copy_file_or_dir(username, host, port,  location, '/home/brett/{}'.format(key), ignore_patterns)
    print("Data sync complete")
    sshStorageAddress = f"{ssh_address}"  # Assuming these variables are accessible here
    
    set_upload_complete_in_db(key, sshStorageAddress, max_cost, image=image)



def run(addr, max_checks=5, max_cost=1.0):
    # parser = argparse.ArgumentParser(description="Send data to an SSH address.")
    # parser.add_argument("--ssh_address", type=str, required=True, help="SSH address to send data to")
    # parser.add_argument("--max_checks", type=int, default=1000, help="Maximum number of checks before declaring failure")
    # args = parser.parse_args()
    main(addr, max_checks, max_cost)

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Send data to an SSH address.")
#     parser.add_argument("--ssh_address", type=str, required=True, help="SSH address to send data to")
#     parser.add_argument("--max_checks", type=int, default=1000, help="Maximum number of checks before declaring failure")
#     args = parser.parse_args()
#     main(args.ssh_address, args.max_checks)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor VastAI instance for startup completion.")
    parser.add_argument("--ssh_address", type=str, required=True, help="SSH address to send data to")
    parser.add_argument("--max_checks", type=int, default=1000, help="Maximum number of checks before declaring failure")
    parser.add_argument("--max_cost", type=float, required=True, help="Maximum hourly hardware cost")
    args = parser.parse_args()
    main(args.ssh_address, args.max_checks, args.max_cost)

    