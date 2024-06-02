import subprocess
import os
import re
import paramiko
from scp import SCPClient

def parse_instance_info(raw_info):
    instance_ids = []
    pattern = r"\n(\d+)"
    matches = re.findall(pattern, raw_info)

    for i, instance_id in enumerate(matches):
        print(f"{i+1}. Instance ID: {instance_id}")
        instance_ids.append(instance_id)

    return instance_ids

def get_ssh_details(vastai_id):
    result = subprocess.run(f"vastai ssh-url {vastai_id}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    ssh_url = result.stdout.strip()
    if ssh_url.startswith('ssh://'):
        ssh_url = ssh_url[6:]
    username, rest = ssh_url.split('@')
    host, port = rest.split(':')
    return username, host, port

def ssh_download_directory(scp, ssh, remote_path, local_base_path):
    cwd = os.getcwd()
    local_base_path = os.path.join(cwd, local_base_path)

    stdin, stdout, stderr = ssh.exec_command(f"find {remote_path} -type f")
    remote_files = stdout.read().decode('utf-8').strip().split('\n')

    for remote_file in remote_files:
        local_file = os.path.join(local_base_path, os.path.relpath(remote_file, remote_path))
        local_dir = os.path.dirname(local_file)

        if not os.path.exists(local_dir):
            os.makedirs(local_dir)

        scp.get(remote_file, local_file)
import subprocess

def open_in_vscode(username, host, port):
    try:
        # Command to open the remote instance in VS Code via Remote SSH
        remote_path = f"{username}@{host}:{port}"
        vscode_command = f"code --folder-uri=vscode-remote://ssh-remote+{remote_path}/root"
        result = subprocess.run(vscode_command, shell=True, check=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("VS Code opened successfully.")
        else:
            print("Failed to open VS Code.")
            print(f"Return code: {result.returncode}")
            print(f"Have {result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


def main():
    raw_info = subprocess.getoutput('vastai show instances')
    instance_ids = parse_instance_info(raw_info)
    choice = int(input("Select an instance by number: "))
    selected_instance_id = instance_ids[choice - 1]
    username, host, port = get_ssh_details(selected_instance_id)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=username)
    
    # with SCPClient(ssh.get_transport()) as scp:
    #     ssh_download_directory(scp, ssh, '/root/results', 'sync_data')

    # ssh.close()
    
    # Open selected remote instance in VS Code
    print(username, host, port)
    open_in_vscode(username, host, port)

# if __name__ == "__main__":
#     main()



def run():
    main()    