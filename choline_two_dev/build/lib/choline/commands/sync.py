import subprocess
import os
import json
import time
import argparse
import platform
import paramiko
from scp import SCPClient
from fnmatch import fnmatch
import traceback
import yaml

def get_choline_yaml_data():
    with open('choline.yaml', 'r') as f:
        data = yaml.safe_load(f)
    return data

def get_choline_json_data():
    with open('choline.json', 'r') as f:
        data = json.load(f)
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

def get_ssh_details(vastai_id):
    result = subprocess.run(f"vastai ssh-url {vastai_id}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    ssh_url = result.stdout.strip()
    if ssh_url.startswith('ssh://'):
        ssh_url = ssh_url[6:]
    username, rest = ssh_url.split('@')
    host, port = rest.split(':')
    return username, host, port

def ssh_copy_new_directories(scp, ssh, local_path, remote_base_path, ignore_patterns, username, host, port):
    timestamp_json_filename = f"file_timestamps_{username}_{host}_{port}.json"
    timestamp_json_path = os.path.join(".choline", timestamp_json_filename)
    
    if os.path.exists(timestamp_json_path):
        with open(timestamp_json_path, "r") as f:
            existing_timestamps = json.load(f)
    else:
        existing_timestamps = {}

    cwd = os.getcwd()

    if os.path.isdir(local_path):
        for root, dirs, files in os.walk(local_path):
            for file_name in files:
                local_file = os.path.join(root, file_name)
                relative_path = os.path.relpath(local_file, cwd)
                if should_ignore(relative_path, ignore_patterns):
                    continue
                last_modified_time = os.path.getmtime(local_file)
                if local_file in existing_timestamps and existing_timestamps[local_file] >= last_modified_time:
                    print(f"The remote and local file {local_file} are the same.")
                    continue
                store_file_timestamp(local_file, username, host, port)
                remote_file = os.path.join(remote_base_path, relative_path).replace('\\', '/')
                remote_dir = os.path.dirname(remote_file)
                stdin, stdout, stderr = ssh.exec_command(f"mkdir -p {remote_dir}")
                stdout.read()
                scp.put(local_file, remote_file)
                print(f"Sent location {local_file}")
    else:
        last_modified_time = os.path.getmtime(local_path)
        if local_path in existing_timestamps and existing_timestamps[local_path] >= last_modified_time:
            print(f"The remote and local file {local_path} are the same.")
            return
        store_file_timestamp(local_path, username, host, port)
        remote_file = os.path.join(remote_base_path, os.path.basename(local_path)).replace('\\', '/')
        scp.put(local_path, remote_file)
        print(f"Sent location {local_path}")


def ssh_copy(username, host, port, src, dest, ignore_patterns):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(host, port=port, username=username)
    with SCPClient(client.get_transport()) as scp:
        ssh_copy_new_directories(scp, client, src, dest, ignore_patterns, username=username, host=host, port=port)
    client.close()

def check_for_choline_txt(vastai_id):
    result = subprocess.run(f"vastai copy {vastai_id}:/root/choline.txt ~/.choline", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(str(result))
    
    if result.returncode != 0 or "Invalid src_id" in result.stdout or "Invalid src_full_path" in result.stdout:
        print("Machine not yet operational. Waiting...")
        return False

    print(f"Detected Operational Machine {vastai_id}.")
    return True


def send_upload_locations(vastai_id, upload_locations, ignore_patterns, max_retries=100):
    username, host, port = get_ssh_details(vastai_id)
    current_path = os.getcwd()
    remote_path = '/root'
    for location in upload_locations:
        retries = 0
        local_path = os.path.join(current_path, location)
        while retries < max_retries:
            try:
                ssh_copy(username, host, port, local_path, remote_path, ignore_patterns)
                
                break
            except Exception as e:
                print(f"Failed to send {location}: {e}. Waiting 20 seconds before retrying.")
                time.sleep(20)
                retries += 1



def main(vastai_id, max_checks):
    choline_data = get_choline_yaml_data()
    ignore_patterns = choline_data.get('ignore', [])
    upload_locations = choline_data.get('upload_locations', [])
    
    checks = 0
    # print("waiting 25 seconds for machine startup...")
    # time.sleep(25)

    while checks < max_checks:
        try:
            if check_for_choline_txt(vastai_id):
                print("Sending Upload Locations")
                send_upload_locations(vastai_id, upload_locations, ignore_patterns)
                print("Data sync complete")
                return

            print("waiting to try again")
            time.sleep(6)
            checks += 1
        except Exception as e:
            print("Error setting up machine. This may not be severe, and we will retry momentarily")
            traceback.print_exc()
            print("trying again in 5 seconds")
            time.sleep(5)
            continue

import re
import subprocess

def parse_instance_info(raw_info):
    instance_ids = []
    pattern = r"\n(\d+)"
    matches = re.findall(pattern, raw_info)

    for i, instance_id in enumerate(matches):
        print(f"{i+1}. Instance ID: {instance_id}")
        instance_ids.append(instance_id)

    return instance_ids


def sync():
    # Get instance information using subprocess
    raw_info = subprocess.getoutput('vastai show instances')

    # Parse the instance IDs
    instance_ids = parse_instance_info(raw_info)

    # Let user select an instance
    choice = int(input("Select an instance by number: "))
    selected_instance_id = instance_ids[choice - 1]

    

    main(selected_instance_id, 20)


if __name__ == "__main__":
    sync()

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Monitor VastAI instance for startup completion.")
#     parser.add_argument("--id", type=str, required=True, help="VastAI instance ID to monitor")
#     parser.add_argument("--max_checks", type=int, default=1000, help="Maximum number of checks before declaring failure")
#     args = parser.parse_args()
    



# def ssh_copy_new_directories(scp, ssh, local_path, remote_base_path, ignore_patterns, username, host, port):
#     timestamp_json_filename = f"file_timestamps_{username}_{host}_{port}.json"
#     timestamp_json_path = os.path.join(".choline", timestamp_json_filename)
    
#     if os.path.exists(timestamp_json_path):
#         with open(timestamp_json_path, "r") as f:
#             existing_timestamps = json.load(f)
#     else:
#         existing_timestamps = {}

#     cwd = os.getcwd()
#     for root, dirs, files in os.walk(local_path):
#         for file_name in files:
#             print(file_name)
#             local_file = os.path.join(root, file_name)
#             relative_path = os.path.relpath(local_file, cwd)
#             if should_ignore(relative_path, ignore_patterns):
#                 continue

#             last_modified_time = os.path.getmtime(local_file)
#             if local_file in existing_timestamps and existing_timestamps[local_file] >= last_modified_time:
#                 print("remote file  and local file {} are the same".format(local_file))
#                 continue

#             print(local_file)
#             store_file_timestamp(local_file, username, host, port)
#             remote_file = os.path.join(remote_base_path, relative_path).replace('\\', '/')
#             remote_dir = os.path.dirname(remote_file)
#             stdin, stdout, stderr = ssh.exec_command(f"mkdir -p {remote_dir}")
#             stdout.read()
#             scp.put(local_file, remote_file)
#             print(f"Sent location {local_file}")


# def ssh_copy(username, host, port, src, dest, ignore_patterns):
#     client = paramiko.SSHClient()
#     client.load_system_host_keys()
#     client.set_missing_host_key_policy(paramiko.WarningPolicy)
#     client.connect(host, port=port, username=username)
#     with SCPClient(client.get_transport()) as scp:
#         if os.path.isdir(src):
#             ssh_copy_new_directories(scp, client, src, dest, ignore_patterns, username=username, host=host, port=port)
#         else:
#             store_file_timestamp(src, username, host, port)
#             remote_file = os.path.join(dest, os.path.basename(src))
#             scp.put(src, remote_file)
#     client.close()
