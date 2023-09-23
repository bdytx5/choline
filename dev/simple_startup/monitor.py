# ### gets run as python monitor --id vastai_id 

# ##### will loop in the background and check for the choline.txt file signifying the completion of the startup script 

# ##### will also check for failures (im not sure exactly how this will work yet 

# import time
# import subprocess
# import os
# import platform
# import argparse

# def check_for_choline_txt(vastai_id):
#     try:
#         subprocess.run(f"vastai copy {vastai_id}:/root/choline.txt ./choline.txt", shell=True, check=True)
#         print(f"Startup script complete. choline.txt found for instance {vastai_id}.")
#         return True
#     except subprocess.CalledProcessError:
#         print("Startup script not yet complete. Waiting...")
#         return False

# def send_alert(message):
#     if platform.system() == "Linux" or platform.system() == "Darwin":
#         os.system(f'echo "{message}" | wall')

# def main(vastai_id, max_checks):
#     checks = 0
#     while checks < max_checks:
#         if check_for_choline_txt(vastai_id):
#             send_alert(f"Instance {vastai_id} has started up.")
#             return
#         time.sleep(60)
#         checks += 1

#     send_alert(f"Instance {vastai_id} has failed to start up.")

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Monitor VastAI instance for startup completion.")
#     parser.add_argument("--id", type=str, required=True, help="VastAI instance ID to monitor")
#     parser.add_argument("--max_checks", type=int, default=30, help="Maximum number of checks before declaring failure")
#     args = parser.parse_args()
#     main(args.id, args.max_checks)

import time
import subprocess
import os
import platform
import argparse
import json

def get_choline_json_data():
    with open('choline.json', 'r') as f:
        data = json.load(f)
    return data

def check_for_choline_txt(vastai_id):
    try:
        subprocess.run(f"vastai copy {vastai_id}:/root/choline.txt ./choline.txt", shell=True, check=True)
        print(f"Startup script complete. choline.txt found for instance {vastai_id}.")
        return True
    except subprocess.CalledProcessError:
        print("Startup script not yet complete. Waiting...")
        return False

def send_alert(message):
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system(f'echo "{message}" | wall')

def send_choline_setup(vastai_id):
    subprocess.run(f"vastai copy ./choline_setup.sh {vastai_id}:/root/choline_setup.sh", shell=True, check=True)

def send_upload_locations(vastai_id, upload_locations):
    for location in upload_locations:
        subprocess.run(f"vastai copy {location} {vastai_id}:/root/", shell=True, check=True)

def main(vastai_id, max_checks):
    checks = 0
    while checks < max_checks:
        if check_for_choline_txt(vastai_id):
            send_alert(f"Instance {vastai_id} has started up. Now setting up environment and syncing data.")
            
            choline_data = get_choline_json_data()
            upload_locations = choline_data.get('upload_locations', [])
            
            send_choline_setup(vastai_id)
            send_upload_locations(vastai_id, upload_locations)
            return
        time.sleep(60)
        checks += 1

    send_alert(f"Instance {vastai_id} has failed to start up.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor VastAI instance for startup completion.")
    parser.add_argument("--id", type=str, required=True, help="VastAI instance ID to monitor")
    parser.add_argument("--max_checks", type=int, default=30, help="Maximum number of checks before declaring failure")
    args = parser.parse_args()
    main(args.id, args.max_checks)