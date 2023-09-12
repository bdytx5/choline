# import requests
# import subprocess
# import os
# import time


# ### writes the choline_{run_id}.txt to the server at ~/.choline/username_runid/ 
# ##### along with all files in working direcotry 

# url = "http://localhost:8000/upload"
# username = "cholineUser"

# # Send the username as form data to the server
# response = requests.post(url, data={'username': username})

# # Extract the destination path from the response
# destination_path = response.text.split(': ')[1].strip()

# # Create the special file with Vast.ai instance information
# run_id = destination_path.split('/')[-1]
# vast_sim_path = os.path.expanduser("~/.choline_vast_sim")
# vast_file_path = os.path.join(destination_path, f"CHOLINE_{run_id}.txt")
# with open(vast_file_path, 'w') as file:
#     file.write(vast_sim_path)

# # Get the current working directory
# source_path = os.getcwd()

# # Construct the rsync command to synchronize files
# command = f'rsync -av {source_path}/ {destination_path}/'

# # Execute the command
# result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# # Print the result
# if result.returncode == 0:
#     print("Files synchronized successfully")
# else:
#     print(f"An error occurred: {result.stderr.decode()}")


import requests
import subprocess
import os
import time

url = "http://localhost:8000/upload"
username = "cholineUser"

# Send the username as form data to the server
response = requests.post(url, data={'username': username})

# Extract the destination path from the response
destination_path = response.text.split(': ')[1].strip()

# Get the current working directory
source_path = os.getcwd()

# Count the total number of files to be sent
total_files = sum([len(files) for _, _, files in os.walk(source_path)]) + 1

# Create the special file with Vast.ai instance information and total files count
run_id = destination_path.split('/')[-1]
vast_sim_path = os.path.expanduser("~/.choline_vast_sim")
vast_file_path = os.path.join(destination_path, f"CHOLINE_{run_id}.txt")
with open(vast_file_path, 'w') as file:
    file.write(f"{vast_sim_path}\n{total_files}")

# Construct the rsync command to synchronize files
command = f'rsync -av {source_path}/ {destination_path}/'

# Execute the command
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Print the result
if result.returncode == 0:
    print("Files synchronized successfully")
else:
    print(f"An error occurred: {result.stderr.decode()}")
