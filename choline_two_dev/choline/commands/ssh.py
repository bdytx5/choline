import re
import subprocess

def parse_instance_info(raw_info):
    """Parse instance information from the raw output of 'vastai show instances'."""
    instance_ids = []
    pattern = r"\n(\d+)"
    matches = re.findall(pattern, raw_info)

    for i, instance_id in enumerate(matches):
        print(f"{i+1}. Instance ID: {instance_id}")
        instance_ids.append(instance_id)

    return instance_ids

def get_ssh_details(vastai_id):
    """Retrieve SSH details (username, host, port) for a given Vast.ai instance ID."""
    result = subprocess.run(f"vastai ssh-url {vastai_id}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    ssh_url = result.stdout.strip()
    if ssh_url.startswith('ssh://'):
        ssh_url = ssh_url[6:]
    username, rest = ssh_url.split('@')
    host, port = rest.split(':')
    return username, host, port

def generate_ssh_command(username, host, port):
    """Generate the SSH command string."""
    ssh_command = f"ssh -p {port} {username}@{host} -L 8080:localhost:8080"
    return ssh_command

def run():
    """Main function to handle the 'ssh' command."""
    raw_info = subprocess.getoutput('vastai show instances')
    instance_ids = parse_instance_info(raw_info)

    if not instance_ids:
        print("No instances found.")
        return

    try:
        choice = int(input("Select an instance by number: "))
        if choice < 1 or choice > len(instance_ids):
            print("Invalid choice.")
            return

        selected_instance_id = instance_ids[choice - 1]
        username, host, port = get_ssh_details(selected_instance_id)

        # Generate and print the SSH command
        ssh_command = generate_ssh_command(username, host, port)
        print("\nUse the following SSH command to connect to the instance:")
        print(ssh_command)
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
