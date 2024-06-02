## takes a map including the GPU requirements as well as the max hourly cost and docker image, and requests the instance 
# ######### this is totally scalable, as it simply listens for events in the db and triggers hardware provisioning scripts 

# import subprocess
# import re
# import os
# import argparse





# def custom_sort_key(offer, expected_storage_gb, expected_runtime_hr, expected_upload_gb=1.0):
#     dph = offer['dph_base']
#     storage_cost_per_hr = (offer['storage_cost'] / (30 * 24)) * expected_storage_gb
#     total_storage_cost = storage_cost_per_hr * expected_runtime_hr
#     download_cost = expected_storage_gb * offer['inet_down_cost']
#     upload_cost = expected_upload_gb * offer['inet_up_cost']
#     total_cost = (dph + storage_cost_per_hr) * expected_runtime_hr + download_cost + upload_cost
    
#     return total_cost





# def sort_offers_by_custom_criteria(offers, expected_storage_gb, expected_runtime_hr):
#     return sorted(offers, key=lambda x: custom_sort_key(x, expected_storage_gb, expected_runtime_hr))



# def create_instance(instance_id, options):
#     command = ["vastai", "create", "instance", str(instance_id)] + options
#     result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     if result.returncode != 0:
#         return None

#     stdout_str = result.stdout.decode()
#     try:
#         match = re.search(r"'new_contract': (\d+)", stdout_str)
#         if match:
#             new_contract = match.group(1)
#             return new_contract
#     except Exception as e:
#         return None

# def run_monitor_instance_script(instance_id, max_checks=30):
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     monitor_script_path = os.path.join(script_dir, "monitor_and_setup_machine.py")
#     subprocess.Popen(["sudo", "python", monitor_script_path, "--id", str(instance_id), "--max_checks", str(max_checks)])

# def main(choline_data, max_hrly_hardware_cost):
#     hardware_filters = choline_data.get('hardware_filters', {})
#     cpu_ram_str = hardware_filters.get('cpu_ram', '')
#     gpu_name = hardware_filters.get('gpu_name', '')
#     disk_space_str = hardware_filters.get('disk_space', '')
#     image = choline_data.get('image', 'python:3.8')
    
#     query = "your_query_here"  # Replace with actual query logic
#     offers = "your_offer_here"  # Replace with actual offer logic
    
#     offers = sort_offers_by_custom_criteria(offers, expected_storage_gb=100, expected_runtime_hr=2)  # Replace with actual values

#     if offers:
#         selected_offer = offers[0]  # Replace with actual selection logic
#         instance_id = selected_offer["id"]
#         options = ["--image", image, "--max_hrly_cost", str(max_hrly_hardware_cost)]
#         contract_id = create_instance(instance_id, options)
        
#         if contract_id:
#             run_monitor_instance_script(instance_id=int(contract_id))

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--max_hrly_hardware_cost', required=True, type=float, help='Maximum hourly hardware cost')
#     args = parser.parse_args()

#     choline_data = {
#         'hardware_filters': {
#             'cpu_ram': '>16',
#             'gpu_name': 'NVIDIA',
#             'disk_space': '>100'
#         },
#         'image': 'python:3.8'
#     }

#     main(choline_data, args.max_hrly_hardware_cost)


