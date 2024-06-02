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

def run_docker_container(image_name):
    try:
        cmd = f"docker run -d --name my_container2 {image_name}"
        subprocess.run(cmd, shell=True, check=True)
        print(f"Started Docker container from image {image_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error while starting Docker container: {e}")

def send_upload_locations(upload_locations, image_name):
    container_name = "my_container2"
    run_docker_container(image_name)
    for location in upload_locations:
        docker_copy(location, container_name, '/root')

def start_docker_if_not_running():
    try:
        subprocess.run(['docker', 'info'], check=True)
    except subprocess.CalledProcessError:
        print("Docker is not running. Attempting to start it.")
        try:
            if platform.system() == "Linux":
                subprocess.run(['sudo', 'systemctl', 'start', 'docker'], check=True)
            elif platform.system() == "Darwin":
                subprocess.run(['open', '--background', '-a', 'Docker'], check=True)
            else:
                print("Unsupported OS for auto-starting Docker")
                return
            print("waiting 20 seconds for docker to start...")
            time.sleep(20)
            print("Docker started successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to start Docker: {e}")

def main(image_name, max_checks):
    start_docker_if_not_running()

    choline_data = get_choline_yaml_data()
    upload_locations = choline_data.get('upload_locations', [])
    
    checks = 0
    
    while checks < max_checks:
        try:
            send_upload_locations(upload_locations, image_name)
            print("Data sync complete")
            return
        except Exception as e:
            print("Exception occurred: ", e)
            traceback.print_exc()
            time.sleep(5)
            checks += 1
            continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start a Docker container and copy files into it.")
    parser.add_argument("--image", type=str, required=True, help="Docker image to start the container from")
    parser.add_argument("--max_checks", type=int, default=1000, help="Maximum number of checks before declaring failure")
    args = parser.parse_args()
    main(args.image, args.max_checks)