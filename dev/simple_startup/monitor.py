# ### gets run as python monitor --id vastai_id 

# ##### will loop in the background and check for the choline.txt file signifying the completion of the startup script 

# ##### will also check for failures  

import time
import subprocess
import os
import platform
import argparse
import json
import os
import time
import subprocess
import os
import os
import time
import subprocess
import paramiko
from scp import SCPClient
import os
import time
import subprocess
import paramiko
from scp import SCPClient
import os
import time
import subprocess
import paramiko
from scp import SCPClient



def get_choline_json_data():
    with open('choline.json', 'r') as f:
        data = json.load(f)
    return data


def check_for_choline_txt(vastai_id):
    result = subprocess.run(f"vastai copy {vastai_id}:/root/choline.txt ./choline.txt", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(str(result))
    
    if result.returncode != 0 or "Invalid src_id" in result.stdout:
        print("Startup script not yet complete. Waiting...")
        return False

    print(f"Startup script complete. choline.txt found for instance {vastai_id}.")
    return True

def send_alert(message):
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system(f'echo "{message}" | wall')


# def send_choline_setup(vastai_id, max_retries=100):
#     print("in send setup script")
#     current_path = os.getcwd()
#     retries = 0
#     while retries < max_retries:
#         result = subprocess.run(f"vastai copy {current_path}/cholineSetupPayload/ {vastai_id}:/root/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         print("res {}".format(str(result)))
#         if result.returncode == 0:
#             print("Sent setup script")
#             break
#         print("Failed to send choline_setup.sh. Waiting 5 seconds before retrying.")
#         time.sleep(5)
#         retries += 1

# def send_upload_locations(vastai_id, upload_locations, max_retries=100):
#     current_path = os.getcwd()
#     for location in upload_locations:
#         retries = 0
#         while retries < max_retries:
#             result = subprocess.run(f"vastai copy {location} {vastai_id}:/root/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#             if result.returncode == 0:
#                 print("Sent location {}".format({current_path}/{location}))
#                 break
#             print(f"Failed to send {location}. Waiting 5 seconds before retrying.")
#             time.sleep(5)
#             retries += 1

#     with open(f'{current_path}/choline_complete.txt', 'w') as f:
#         f.write('0')

#     retries = 0
#     while retries < max_retries:
#         result = subprocess.run(f"vastai copy {current_path}/choline_complete.txt {vastai_id}:/root/choline_complete.txt", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         if result.returncode == 0:
#             break
#         print("Failed to send choline_complete.txt. Waiting 5 seconds before retrying.")
#         time.sleep(5)
#         retries += 1


def get_ssh_details(vastai_id):
    result = subprocess.run(f"vastai ssh-url {vastai_id}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    ssh_url = result.stdout.strip()
    if ssh_url.startswith('ssh://'):
        ssh_url = ssh_url[6:]
    username, rest = ssh_url.split('@')
    host, port = rest.split(':')
    return username, host, port

def ssh_copy_directory(scp, ssh, local_path, remote_base_path):
    cwd = os.getcwd()
    for root, dirs, files in os.walk(local_path):
        for file_name in files:
            local_file = os.path.join(root, file_name)
            relative_path = os.path.relpath(local_file, cwd)
            remote_file = os.path.join(remote_base_path, relative_path).replace('\\','/')
            remote_dir = os.path.dirname(remote_file)
            
            stdin, stdout, stderr = ssh.exec_command(f"mkdir -p {remote_dir}")
            stdout.read()
            
            scp.put(local_file, remote_file)

def ssh_copy(username, host, port, src, dest):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(host, port=port, username=username)
    with SCPClient(client.get_transport()) as scp:
        if os.path.isdir(src):
            ssh_copy_directory(scp, client, src, dest)
        else:
            relative_path = os.path.relpath(src, os.getcwd())
            remote_file = os.path.join(dest, relative_path)
            scp.put(src, remote_file)
    client.close()

def send_choline_setup(vastai_id, max_retries=100):
    username, host, port = get_ssh_details(vastai_id)
    current_path = os.getcwd()
    local_path = os.path.join(current_path, 'cholineSetupPayload')
    remote_path = '/root'
    retries = 0
    while retries < max_retries:
        try:
            ssh_copy(username, host, port, local_path, remote_path)
            print("Sent setup script")
            break
        except Exception as e:
            print(f"Failed to send choline_setup: {e}. Waiting 5 seconds before retrying.")
            time.sleep(5)
            retries += 1

def send_upload_locations(vastai_id, upload_locations, max_retries=100):
    username, host, port = get_ssh_details(vastai_id)
    current_path = os.getcwd()
    remote_path = '/root'
    for location in upload_locations:
        retries = 0
        local_path = os.path.join(current_path, location)
        while retries < max_retries:
            try:
                ssh_copy(username, host, port, local_path, remote_path)
                print(f"Sent location {local_path}")
                break
            except Exception as e:
                print(f"Failed to send {location}: {e}. Waiting 5 seconds before retrying.")
                time.sleep(5)
                retries += 1

    complete_file = os.path.join(current_path, 'choline_complete.txt')
    with open(complete_file, 'w') as f:
        f.write('0')

    retries = 0
    while retries < max_retries:
        try:
            ssh_copy(username, host, port, complete_file, remote_path)
            print("Sent choline_complete.txt")
            break
        except Exception as e:
            print(f"Failed to send choline_complete.txt: {e}. Waiting 5 seconds before retrying.")
            time.sleep(5)
            retries += 1

def main(vastai_id, max_checks):
    checks = 0
    while checks < max_checks:
        try:
            if check_for_choline_txt(vastai_id):
                # send_alert(f"Instance {vastai_id} has started up. Now setting up environment and syncing data.")
                
                choline_data = get_choline_json_data()
                upload_locations = choline_data.get('upload_locations', [])
                print("waiting 120 seconds for machine startup")
                time.sleep(75)
                print("continuing to send set up")
                send_choline_setup(vastai_id)
                send_upload_locations(vastai_id, upload_locations)
                return
            print("waiting to try again")
            time.sleep(6)
            checks += 1
        except Exception as e:
            print("exc {}".format(str(e)))
            print("trying in 5")
            time.sleep(5)   
            continue

    send_alert(f"Instance {vastai_id} has failed to start up.")

import unittest
import os

# class TestVastaiSSHFunctions(unittest.TestCase):
#     def test_send_choline_setup(self):
#         instance_id = "7093888"  # Replace with your instance ID
#         send_choline_setup(instance_id)
#         # Check logs or destination to confirm file has been transferred
        
#     def test_send_upload_locations(self):
#         instance_id = "7093888"  # Replace with your instance ID
#         upload_locations = ["/Users/brettyoung/Desktop/dev/choline/dev/simple_startup/test_payload"]  # Replace with your test file name
#         send_upload_locations(instance_id, upload_locations)
#         # Check logs or destination to confirm file has been transferred

#     def test_all(self):
#         self.test_send_choline_setup()
#         self.test_send_upload_locations()

# if __name__ == '__main__':
#     unittest.main()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor VastAI instance for startup completion.")
    parser.add_argument("--id", type=str, required=True, help="VastAI instance ID to monitor")
    parser.add_argument("--max_checks", type=int, default=30, help="Maximum number of checks before declaring failure")
    args = parser.parse_args()
    main(args.id, args.max_checks)