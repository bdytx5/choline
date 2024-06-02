import subprocess
import os
import json
import time
import argparse
import platform
import paramiko
import yaml 
import traceback

def get_choline_yaml_data():
    with open('choline.yaml', 'r') as f:
        data = yaml.safe_load(f)
    return data

def send_alert(message):
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system(f'echo "{message}" | wall')

def docker_copy(local_path, container_name, remote_path):
    try:
        cmd = f"docker cp {local_path} {container_name}:{remote_path}"
        subprocess.run(cmd, shell=True, check=True)
        print(f"Copied {local_path} to {container_name}:{remote_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error while copying files to Docker container: {e}")

def docker_copy_choline_dir(local_path, container_name, remote_base_path):
    for root, dirs, files in os.walk(local_path):
        for file_name in files:
            local_file = os.path.join(root, file_name)
            remote_file = os.path.join(remote_base_path, os.path.relpath(local_file, local_path))
            docker_copy(local_file, container_name, remote_file)

def docker_start_container(vastai_id, image_name):
    container_name = f"vastai_{vastai_id}"
    try:
        cmd = f"docker run -d --name {container_name} {image_name}"
        subprocess.run(cmd, shell=True, check=True)
        print(f"Started Docker container {container_name} from image {image_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error while starting Docker container: {e}")

def send_upload_locations(vastai_id, upload_locations, image_name):
    container_name = f"vastai_{vastai_id}"
    docker_start_container(vastai_id, image_name)
    for location in upload_locations:
        docker_copy(location, container_name, '/root')

def main(vastai_id, image_name, max_checks):
    choline_data = get_choline_yaml_data()
    upload_locations = choline_data.get('upload_locations', [])
    
    checks = 0
    # print("waiting 25 seconds for machine startup...")
    # time.sleep(25)
    
    while checks < max_checks:
        try:
            send_upload_locations(vastai_id, upload_locations, image_name)
            print("Data sync complete")
            return
        except Exception as e:
            print("Exception occurred: ", e)
            traceback.print_exc()
            time.sleep(5)
            checks += 1
            continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor VastAI instance for startup completion.")
    parser.add_argument("--id", type=str, required=True, help="VastAI instance ID to monitor")
    parser.add_argument("--image", type=str, required=True, help="Docker image to start the container from")
    parser.add_argument("--max_checks", type=int, default=1000, help="Maximum number of checks before declaring failure")
    args = parser.parse_args()
    main(args.id, args.image, args.max_checks)