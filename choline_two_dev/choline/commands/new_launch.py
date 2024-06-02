import os
import json
import subprocess
import time
import argparse
import yaml
import paramiko
import zipfile
from scp import SCPClient
from fnmatch import fnmatch


def read_setup_from_choline_yaml_and_write_sh_to_disk():
    choline_data = get_choline_yaml_data()
    setup_script = choline_data.get('setup_script', '')
    cwd = os.getcwd()
    setup_script_path = os.path.join(cwd, ".choline", "choline_setup.sh")

    with open(setup_script_path, "w") as f:
        f.write(setup_script)

    return setup_script_path


def pretty_print_offer(offer, index):
    print(f"########### VASTAI OFFERS {index + 1} ###########")
    print(f"GPU MODEL: {offer['gpu_name']}")
    print(f"VRAM: {offer['gpu_ram']}")
    print(f"cpu RAM: {offer['cpu_ram']}")
    print(f"Cost per hour: {offer['dph_base']}")
    print(f"Internet download speed: {offer['inet_down']}")
    print(f"Internet upload speed: {offer['inet_up']}")
    print(f"cuda: {offer['cuda_max_good']}")
    print(f"DL Performance: {offer['dlperf']}")
    print(f"Reliability: {offer['reliability2']}")
    print(f"Storage cost: {offer['storage_cost']}")
    print(f"Internet download cost: {offer['inet_down_cost']}")
    print(f"Internet upload cost: {offer['inet_up_cost']}")
    print("#######################################\n\n")


def get_choline_yaml_data():
    with open('./choline.yaml', 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
    return data


def zip_directory(source_dir, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)


def ssh_copy(username, host, port, src, dest):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.connect(host, port=port, username=username)

    zip_name = 'transfer.zip'
    zip_directory(src, zip_name)

    with SCPClient(client.get_transport()) as scp:
        remote_zip_path = os.path.join(dest, zip_name)
        scp.put(zip_name, remote_zip_path)

    client.close()
    os.remove(zip_name)


def generate_vast_onstart_script():
    choline_dir = os.path.join(os.getcwd(), ".choline")
    if not os.path.exists(choline_dir):
        os.makedirs(choline_dir)

    script_lines = [
        "#!/bin/bash",
        "mkdir -p ~/.choline",
        "echo '0' > ~/choline.txt",
        "while [ ! -f ~/.choline/choline_setup.sh ]; do",
        "  sleep 1",
        "done",
        "sleep 5",
        "echo 'running setup script' > ~/choline.txt",
        "unzip -o ~/.choline/transfer.zip -d ~/.choline && rm ~/.choline/transfer.zip",
        ". ~/.choline/choline_setup.sh >> ~/.choline/choline_setup_log.txt 2>&1",
    ]

    script_content = "\n".join(script_lines)
    setup_script_path = os.path.join(choline_dir, "choline_onstart.sh")

    with open(setup_script_path, "w") as f:
        f.write(script_content)

    return setup_script_path


def search_offers(additional_query=""):
    query = f""
    if additional_query:
        query = f"{query} {additional_query}"

    command = ["vastai", "search", "offers", "--raw", query]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Error in search:", result.stderr.decode())
        return []

    offers = json.loads(result.stdout.decode())
    return offers


def custom_sort_key(offer, expected_storage_gb, expected_runtime_hr, expected_upload_gb=1.0):
    dph = offer['dph_base']
    storage_cost_per_hr = (offer['storage_cost'] / (30 * 24)) * expected_storage_gb
    total_storage_cost = storage_cost_per_hr * expected_runtime_hr
    download_cost = expected_storage_gb * offer['inet_down_cost']
    upload_cost = expected_upload_gb * offer['inet_up_cost']
    total_cost = (dph + storage_cost_per_hr) * expected_runtime_hr + download_cost + upload_cost
    return total_cost


def sort_offers_by_custom_criteria(offers, expected_storage_gb, expected_runtime_hr):
    return sorted(offers, key=lambda x: custom_sort_key(x, expected_storage_gb, expected_runtime_hr))


def create_instance(instance_id, options):
    command = ["vastai", "create", "instance", str(instance_id)] + options
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Error in instance creation:", result.stderr.decode())
        return None

    stdout_str = result.stdout.decode()
    try:
        match = re.search(r"'new_contract': (\d+)", stdout_str)
        if match:
            new_contract = match.group(1)
        else:
            print("Failed to find new contract ID.")
            return None
    except Exception as e:
        print(f"Error while parsing: {e}")
        return None

    print("Instance created successfully.")
    return new_contract


def check_for_choline_txt(vastai_id):
    try:
        command = f"vastai execute {vastai_id} 'ls -l /root/'"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            output = result.stdout.strip()
            if 'choline.txt' in output:
                print(f"Detected Operational Machine with choline.txt present: {vastai_id}.")
                return True
            else:
                print(f"choline.txt not found in /root/ on Machine {vastai_id}.")
                return False
        else:
            print(f"Failed to execute command on Machine {vastai_id}. Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return False


def get_ssh_details(vastai_id):
    result = subprocess.run(f"vastai ssh-url {vastai_id}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    ssh_url = result.stdout.strip()
    if ssh_url.startswith('ssh://'):
        ssh_url = ssh_url[6:]
    username, rest = ssh_url.split('@')
    host, port = rest.split(':')
    return username, host, port


def run_monitor_instance_script_vast(instance_id, max_checks=300):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    monitor_script_path = os.path.join(script_dir, "monitor_and_setup_machine.py")
    print("waiting 25 seconds for machine startup...")
    time.sleep(25)
    checks = 0
    while checks < max_checks:
        try:
            if check_for_choline_txt(instance_id):
                u, h, p = get_ssh_details(instance_id)
                uhp_str = "{},{},{}".format(u, h, p)
                subprocess.Popen(["sudo", "python", monitor_script_path, "--uhp", uhp_str, "--max_checks", str(max_checks)])
                print("Data sync complete")
                return
            print("waiting to try again")
            time.sleep(6)
            checks += 1
        except Exception as e:
            time.sleep(5)
            import traceback
            print("Error setting up machine. This may not be severe, and we will retry momentarily")
            traceback.print_exc()
            if checks >= max_checks:
                print("failed to setup machine. We recommend you try to launch a different machine, as this is likely an issue with the machine")


def main():
    choline_data = get_choline_yaml_data()
    hardware_filters = choline_data.get('hardware_filters', {})
    cpu_ram_str = hardware_filters.get('cpu_ram', '')
    gpu_name = hardware_filters.get('gpu_name', '')
    disk_space_str = hardware_filters.get('disk_space', '')
    image = choline_data.get('image', 'python:3.8')
    num_gpus = choline_data.get('num_gpus', '1')
    startup_script_path = generate_vast_onstart_script()
    read_setup_from_choline_yaml_and_write_sh_to_disk()

    match = re.match(r"([<>!=]+)(\d+)", cpu_ram_str)
    if match:
        cpu_ram_operator, cpu_ram_value = match.groups()
        cpu_ram_value = int(cpu_ram_value)
    else:
        print("Invalid CPU RAM string in JSON. Using default values.")
        return

    match = re.match(r"([<>!=]+)(\d+)", disk_space_str)
    if match:
        disk_space_operator, disk_space_value = match.groups()
        disk_space_value = int(disk_space_value)
    else:
        print("Invalid disk_space string in JSON. Using default values.")
        return

    if gpu_name.lower() != 'any':
        query = f"gpu_name={gpu_name} num_gpus>={num_gpus} disk_space {disk_space_operator} {disk_space_value} cpu_ram > {cpu_ram_value}"
    else:
        query = f"disk_space {disk_space_operator} {disk_space_value} cpu_ram > {cpu_ram_value}"

    offers = search_offers(query)
    exp_storage = disk_space_value
    offers = sort_offers_by_custom_criteria(offers, expected_storage_gb=exp_storage, expected_runtime_hr=2)

    if offers:
        print("Five cheapest offers:")
        for i, offer in enumerate(offers[:20]):
            pretty_print_offer(offer, i)

        choice = int(input("Select an offer by entering its number (1-5): ")) - 1
        selected_offer = offers[choice]
        pretty_print_offer(selected_offer, choice)

        confirmation = input("Would you like to proceed? (y/n): ")
        if confirmation.lower() == 'y':
            instance_id = selected_offer["id"]
            options = ["--image", image, "--disk", str(disk_space_value), "--onstart", startup_script_path, "--env", "-e TZ=PDT -e XNAME=XX4 -p 22:22 -p 5000:5000"]
            contract_id = create_instance(instance_id, options)
            run_monitor_instance_script_vast(instance_id=int(contract_id))
            print(f"Instance creation request complete. Now setting up your instance with id {instance_id}. Run 'choline status 'instance id'' to check the logs for your setup.")
        else:
            print("Operation canceled.")
    else:
        print("No suitable offers found.")


if __name__ == "__main__":
    main()
