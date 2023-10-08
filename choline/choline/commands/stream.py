# import subprocess
# import os
# import re
# import time

# def parse_instance_info(raw_info):
#     instance_ids = []
#     pattern = r"\n(\d+)"
#     matches = re.findall(pattern, raw_info)

#     for i, instance_id in enumerate(matches):
#         print(f"{i+1}. Instance ID: {instance_id}")
#         instance_ids.append(instance_id)

#     return instance_ids

# def main():
#     # Get instance information using subprocess
#     raw_info = subprocess.getoutput('vastai show instances')

#     # Parse the instance IDs
#     instance_ids = parse_instance_info(raw_info)

#     # Let user select an instance
#     choice = int(input("Select an instance by number: "))
#     selected_instance_id = instance_ids[choice - 1]

#     last_position = 0

#     while True:
#         # Run vastai copy command to get the log.txt
#         subprocess.run(f"vastai copy {selected_instance_id}:/root/log.txt .", 
#                        shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

#         # Read and display the new lines from log.txt
#         with open("log.txt", 'r') as f:
#             f.seek(last_position)
#             new_data = f.read()
#             last_position = f.tell()
#             if new_data:
#                 print(new_data.strip())
        
#         # Delete the log.txt file
#         os.remove("log.txt")

#         # Pause for a bit before looping again
#         time.sleep(5)

# if __name__ == "__main__":
#     main()

import subprocess
import os
import re
import paramiko
from scp import SCPClient
import time

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

def main():
    # Get instance information using subprocess
    raw_info = subprocess.getoutput('vastai show instances')

    # Parse the instance IDs
    instance_ids = parse_instance_info(raw_info)

    # Let user select an instance
    choice = int(input("Select an instance by number: "))
    selected_instance_id = instance_ids[choice - 1]
    username, host, port = get_ssh_details(selected_instance_id)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=username)

    last_position = 0

    try:
        with SCPClient(ssh.get_transport()) as scp:
            while True:
                scp.get('/root/log.txt', 'log.txt')

                # Read and display the new lines from log.txt
                with open("log.txt", 'r') as f:
                    f.seek(last_position)
                    new_data = f.read()
                    last_position = f.tell()
                    if new_data:
                        print(new_data.strip())

                # Delete the local log.txt file
                os.remove("log.txt")

                # Pause for a bit before looping again
                time.sleep(5)
    finally:
        ssh.close()

# if __name__ == "__main__":
#     main()


def run():
    main()    