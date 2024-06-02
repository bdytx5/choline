# ### gets run as python monitor --id vastai_id 

# ##### will loop in the background and check for the choline.txt file signifying the completion of the startup script 

# ##### will also check for failures  

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

import unittest
import os
from scp import SCPClient, SCPException
import re
print("Exception traceback:")
traceback.print_exc()

import os
from scp import SCPClient, SCPException

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


##### for checking diffs between last run 
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
            # print("making remote dir")
            stdin, stdout, stderr = ssh.exec_command(f"mkdir -p {remote_dir}")
            stdout.read()
            print("local = {} remote destin = {}".format(local_file, remote_file))
            try:
                scp.put(local_file, remote_file)
            except SCPException as e:
                print(f"SCP Exception for {remote_file}: {str(e)}")
                print("Error details: ", stderr.read().decode())


def should_ignore(file, ignore_patterns):
    # Your logic to check if a file should be ignored
    return False

def store_file_timestamp(local_file, username, host, port):
    # Your logic to store file timestamps
    pass

def progress(filename, size, sent):
    percentage = (float(sent) / float(size)) * 100
    bar_length = 40
    block = int(round(bar_length * percentage / 100))
    text = f"\rProgress: [{'#' * block}{'.' * (bar_length - block)}] {percentage:.2f}%"
    print(text, end='')


def ssh_copy_choline_dir(scp, ssh, local_path, remote_base_path, ignore_patterns, username, host, port):
    #### sends .choline to /root/ 
    last_folder = os.path.basename(os.path.normpath(local_path))
    new_remote_base_path = os.path.join(remote_base_path, last_folder)
    
    for root, dirs, files in os.walk(local_path):
        for file_name in files:
            local_file = os.path.join(root, file_name)
            
            if should_ignore(local_file, ignore_patterns):
                continue
            
            # Store the file's timestamp before uploading
            store_file_timestamp(local_file, username, host, port)
            
            remote_file = os.path.join(new_remote_base_path, os.path.relpath(local_file, local_path))
            remote_dir = os.path.dirname(remote_file)
            
            stdin, stdout, stderr = ssh.exec_command(f"mkdir -p {remote_dir}")
            stdout.read()
            
            print("local = {} remote destin = {}".format(local_file, remote_file))
            try:
                scp.put(local_file, remote_file)
            except SCPException as e:
                print(f"SCP Exception for {remote_file}: {str(e)}")
                print("Error details: ", stderr.read().decode())


def ssh_copy_choline(username, host, port, src, dest, ignore_patterns):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(host, port=port, username=username)
    with SCPClient(client.get_transport(), progress=progress) as scp:
        if os.path.isdir(src):
            ssh_copy_choline_dir(scp, client, src, dest, ignore_patterns, username=username, host=host, port=port)



def ssh_copy(username, host, port, src, dest, ignore_patterns):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(host, port=port, username=username)
    with SCPClient(client.get_transport(), progress=progress) as scp:
        if os.path.isdir(src):
            ssh_copy_directory_full_path(scp, client, src, dest, ignore_patterns, username=username, host=host, port=port)
        else:
            # store_file_timestamp(src, username, host, port)
            # remote_file = os.path.join(dest, os.path.basename(src))
            # scp.put(src, remote_file)
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


def check_for_choline_txt(vastai_id):
    result = subprocess.run(f"vastai copy {vastai_id}:/root/choline.txt ~/.choline", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(str(result))
    
    if result.returncode != 0 or "Invalid src_id" in result.stdout or "Invalid src_full_path" in result.stdout:
        print("Machine not yet operational. Waiting...")
        return False

    print(f"Detected Operational Machine {vastai_id}.")
    return True





def send_upload_locations(uhr_str, upload_locations, ignore_patterns, max_retries=100):
    username, host, port = uhr_str.split(",")
    current_path = os.getcwd()
    remote_path = '/root'
    for location in upload_locations:
        retries = 0
        # local_path = os.path.join(current_path, location)
        while retries < max_retries:
            try:
                # ssh_copy(username, host, port, local_path, remote_path, ignore_patterns)
                ssh_copy(username, host, port, location, remote_path, ignore_patterns)
                print(f"Sent location {location}")
                break
            except Exception as e:
                print(f"Failed to send {location}: {e}. Waiting 20 seconds before retrying.")
                time.sleep(20)
                retries += 1

    choline_dir = os.path.join(os.getcwd(), '.choline')
    
    ssh_copy_choline(username, host, port, choline_dir, remote_path, ignore_patterns)




def main(uhr_str, max_checks):
    choline_data = get_choline_yaml_data()
    ignore_patterns = choline_data.get('ignore', [])
    upload_locations = choline_data.get('upload_locations', [])
    
    checks = 0

    # print("waiting 25 seconds for machine startup...")
    # time.sleep(25)
    send_upload_locations(uhr_str, upload_locations, ignore_patterns) # transer required data 
    print("Data sync complete")
    # while checks < max_checks:
    #     try:
    #         if check_for_choline_txt(vastai_id): # signifys machine is operational 
    #             print("Sending Upload Locations")
    #             send_upload_locations(vastai_id, upload_locations, ignore_patterns) # transer required data 
    #             print("Data sync complete")
    #             return
            
    #         print("waiting to try again")
    #         time.sleep(6)
    #         checks += 1
    #     except Exception as e:
    #         import traceback
    #         print("Error setting up machine. This may not be severe, and we will retry momentarily")
    #         traceback.print_exc()

    #         if checks >= max_checks:
    #             print("failed to setup machine. We reccomend you try to launch a different machine, as this is likely an issue with the machine")
    #             send_alert(f"Instance {vastai_id} has failed to start up.")


    #         print("trying again in 5 seconds")
    #         time.sleep(5)
    #         continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor VastAI instance for startup completion.")
    parser.add_argument("--uhp", type=str, required=True, help="usenername,host,port")
    parser.add_argument("--max_checks", type=int, default=1000, help="Maximum number of checks before declaring failure")
    args = parser.parse_args()
    main(args.uhp, args.max_checks)





# def send_choline_setup(vastai_id, max_retries=100):
#     # needs to read the setup script from choline.yaml and write it to .choline/choline_setup.sh then send it 
#     username, host, port = get_ssh_details(vastai_id)
#     current_path = os.getcwd()
#     local_path = os.path.join(current_path, '.choline')
#     remote_path = '/root'
#     retries = 0
#     while retries < max_retries:
#         try:
#             ssh_copy(username, host, port, local_path, remote_path)
#             print("Sent setup script")
#             break
#         except Exception as e:
#             print(f"Failed to send choline_setup: {e}. Waiting 5 seconds before retrying.")
#             time.sleep(5)
#             retries += 1







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


# def ssh_copy_directory(scp, ssh, local_path, remote_base_path):
#     ignore_patterns = read_cholineignore()
#     cwd = os.getcwd()
#     for root, dirs, files in os.walk(local_path):
#         for file_name in files:
#             local_file = os.path.join(root, file_name)
#             relative_path = os.path.relpath(local_file, cwd)
#             if should_ignore(relative_path, ignore_patterns):
#                 continue
#             remote_file = os.path.join(remote_base_path, relative_path).replace('\\', '/')
#             remote_dir = os.path.dirname(remote_file)
            
#             stdin, stdout, stderr = ssh.exec_command(f"mkdir -p {remote_dir}")
#             stdout.read()
#             scp.put(local_file, remote_file)

# def ssh_copy_directory(scp, ssh, local_path, remote_base_path, ignore_patterns):
#     cwd = os.getcwd()
#     for root, dirs, files in os.walk(local_path):
#         for file_name in files:
#             local_file = os.path.join(root, file_name)
#             relative_path = os.path.relpath(local_file, cwd)
#             if should_ignore(relative_path, ignore_patterns):
#                 continue

#             store_file_timestamp(local_file) #

#             remote_file = os.path.join(remote_base_path, relative_path).replace('\\', '/')
#             remote_dir = os.path.dirname(remote_file)
            
#             stdin, stdout, stderr = ssh.exec_command(f"mkdir -p {remote_dir}")
#             stdout.read()
#             scp.put(local_file, remote_file)



# def ssh_copy(username, host, port, src, dest):
#     client = paramiko.SSHClient()
#     client.load_system_host_keys()
#     client.set_missing_host_key_policy(paramiko.WarningPolicy)
#     client.connect(host, port=port, username=username)
#     with SCPClient(client.get_transport()) as scp:
#         if os.path.isdir(src):
#             ssh_copy_directory(scp, client, src, dest)
#         else:
#             relative_path = os.path.relpath(src, os.getcwd())
#             remote_file = os.path.join(dest, relative_path)
#             scp.put(src, remote_file)
#     client.close()


# def ssh_copy(username, host, port, src, dest, ignore_patterns):
#     client = paramiko.SSHClient()
#     client.load_system_host_keys()
#     client.set_missing_host_key_policy(paramiko.WarningPolicy)
#     client.connect(host, port=port, username=username)
#     with SCPClient(client.get_transport()) as scp:
#         if os.path.isdir(src):
#             ssh_copy_directory(scp, client, src, dest, ignore_patterns, username=username, host=host,port=port)
#         else:
#             relative_path = os.path.relpath(src, os.getcwd())
#             store_file_timestamp(src, username, host, port)
#             remote_file = os.path.join(dest, relative_path)
#             scp.put(src, remote_file)
#     client.close()


# def ssh_copy_directory(scp, ssh, local_path, remote_base_path, ignore_patterns, username, host, port):
#     cwd = os.getcwd()
#     for root, dirs, files in os.walk(local_path):
#         for file_name in files:
#             local_file = os.path.join(root, file_name)
#             relative_path = os.path.relpath(local_file, cwd)
            
#             if should_ignore(relative_path, ignore_patterns):
#                 continue
            
#             # Store the file's timestamp before uploading
#             store_file_timestamp(local_file, username, host, port)
            
#             remote_file = os.path.join(remote_base_path, relative_path).replace('\\', '/')
#             remote_dir = os.path.dirname(remote_file)
            
#             stdin, stdout, stderr = ssh.exec_command(f"mkdir -p {remote_dir}")
#             stdout.read()
#             print("local = {} remote destin = {}".format(local_file, remote_file))
#             scp.put(local_file, remote_file)




# def ssh_copy_directory(scp, ssh, local_path, remote_base_path, ignore_patterns, username, host, port):
#     cwd = os.getcwd()
#     for root, dirs, files in os.walk(local_path):
#         for file_name in files:
#             local_file = os.path.join(root, file_name)
#             relative_path = os.path.relpath(local_file, cwd)
            
#             if should_ignore(relative_path, ignore_patterns):
#                 continue
            
#             # Store the file's timestamp before uploading
#             store_file_timestamp(local_file, username, host, port)
            
#             remote_file = os.path.join(remote_base_path, relative_path).replace('\\', '/')
#             remote_file = re.sub(r'(\.\./)+', '', remote_file)  # Replace any sequence of ../ with /root/
#             remote_dir = os.path.dirname(remote_file)
            
#             stdin, stdout, stderr = ssh.exec_command(f"mkdir -p {remote_dir}")
#             stdout.read()
#             print("local = {} remote destin = {}".format(local_file, remote_file))
#             scp.put(local_file, remote_file)



##################### 

# import subprocess
# import os
# import json
# import time
# import argparse
# import platform
# import yaml
# import traceback
# from fnmatch import fnmatch

# # Load YAML data from a file
# def get_choline_yaml_data():
#     with open('choline.yaml', 'r') as f:
#         data = yaml.safe_load(f)
#     return data

# # Load JSON data from a file
# def get_choline_json_data():
#     with open('choline.json', 'r') as f:
#         data = json.load(f)
#     return data

# # Send an alert message
# def send_alert(message):
#     if platform.system() in ["Linux", "Darwin"]:
#         os.system(f'echo "{message}" | wall')

# # Store the file's timestamp before uploading
# def store_file_timestamp(file_path, vastai_id, choline_dir=".choline"):
#     timestamp_json_filename = f"file_timestamps_{vastai_id}.json"
#     timestamp_json_path = os.path.join(choline_dir, timestamp_json_filename)
#     last_modified_time = os.path.getmtime(file_path)

#     if os.path.exists(timestamp_json_path):
#         with open(timestamp_json_path, "r") as f:
#             file_data = json.load(f)
#     else:
#         file_data = {}

#     file_data[file_path] = last_modified_time

#     with open(timestamp_json_path, "w") as f:
#         json.dump(file_data, f)

# # Check if a file should be ignored based on patterns
# def should_ignore(path, ignore_patterns):
#     for pattern in ignore_patterns:
#         if fnmatch(path, pattern):
#             return True
#     return False

# # Function to copy files or directories using vastai copy
# def vastai_copy(vastai_id, src, dest, ignore_patterns):
#     if os.path.isdir(src):
#         for root, dirs, files in os.walk(src):
#             for file_name in files:
#                 local_file = os.path.join(root, file_name)
#                 if should_ignore(local_file, ignore_patterns):
#                     continue
#                 store_file_timestamp(local_file, vastai_id)
#                 remote_file = os.path.join(dest, os.path.relpath(local_file, src)).replace('\\', '/')
#                 result = subprocess.run(f"vastai copy {local_file} {vastai_id}:{remote_file}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#                 if result.returncode != 0:
#                     raise Exception(f"Failed to copy {local_file} to {vastai_id}:{remote_file}. Error: {result.stderr}")
#     else:
#         store_file_timestamp(src, vastai_id)
#         remote_file = os.path.join(dest, os.path.basename(src))
#         result = subprocess.run(f"vastai copy {src} {vastai_id}:{remote_file}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         if result.returncode != 0:
#             raise Exception(f"Failed to copy {src} to {vastai_id}:{remote_file}. Error: {result.stderr}")

# # Function to check if the choline.txt file exists on the remote machine
# def check_for_choline_txt(vastai_id):
#     result = subprocess.run(f"vastai copy {vastai_id}:/root/choline.txt ~/.choline", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     print(str(result))

#     if result.returncode != 0 or "Invalid src_id" in result.stdout or "Invalid src_full_path" in result.stdout:
#         print("Machine not yet operational. Waiting...")
#         return False

#     print(f"Detected Operational Machine {vastai_id}.")
#     return True

# # Function to send upload locations
# def send_upload_locations(vastai_id, upload_locations, ignore_patterns, max_retries=100):
#     remote_path = '/root'
#     for location in upload_locations:
#         retries = 0
#         while retries < max_retries:
#             try:
#                 vastai_copy(vastai_id, location, remote_path, ignore_patterns)
#                 print(f"Sent location {location}")
#                 break
#             except Exception as e:
#                 print(f"Failed to send {location}: {e}. Waiting 20 seconds before retrying.")
#                 time.sleep(20)
#                 retries += 1

#     choline_dir = os.path.join(os.getcwd(), '.choline')
#     vastai_copy(vastai_id, choline_dir, remote_path, ignore_patterns)

# # Main function
# def main(vastai_id, max_checks):
#     choline_data = get_choline_yaml_data()
#     ignore_patterns = choline_data.get('ignore', [])
#     upload_locations = choline_data.get('upload_locations', [])

#     send_upload_locations(vastai_id, upload_locations, ignore_patterns)
#     print("Data sync complete")

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Monitor VastAI instance for startup completion.")
#     parser.add_argument("--vastai_id", type=str, required=True, help="VastAI instance ID")
#     parser.add_argument("--max_checks", type=int, default=1000, help="Maximum number of checks before declaring failure")
#     args = parser.parse_args()
#     main(args.vastai_id, args.max_checks)
