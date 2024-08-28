

# # import subprocess
# # ########### t0d0 -> add monitoring for failures and if so, shutdown and get a new instance 
# # ################# need to get the instance ID from the choline launch in order to manage it 
    
# # ############################ 


# # # how to import launch 
# # # from . import launch  # Relative import


# # # def main():
# # #     max_price = float(input("Enter the maximum hourly price you are willing to pay: "))
# # #     # launch_module.bid(max_price)
# # #     subprocess.run(["sudo", "choline", "launch", str(max_price)])

# # # def run():
# # #     main()




# # from . import launch  # Relative import

# # def main():
# #     max_price = float(input("Enter the maximum hourly price you are willing to pay: "))
# #     instance_generator = launch.main(max_price=max_price)
    
# #     for instance_id in instance_generator:
# #         print(f"Instance ID: {instance_id}")
# #         # Continue with other logic here if needed

# #         ##### need to put the monitoring logic in here 

# # def run():
# #     main()

# # # soooo clean 


# # # from . import launch  # Relative import


# # # ########### t0d0 -> add monitoring for failures and if so, shutdown and get a new instance  
    

# # # def main():
# # #     max_price = float(input("Enter the maximum hourly price you are willing to pay: "))

# # #     instance_generator = launch.main(max_price=max_price)
# # #     try:
# # #         instance_id = next(instance_generator)
# # #         print(f"Instance ID: {instance_id}")
# # #     except StopIteration:
# # #         print("No instance ID was generated.")

# # # def run():
# # #     main()




# # # from . import launch  # Relative import
# # # import subprocess
# # # import time

# # # def monitor_instance(instance_id):
# # #     """Monitor the instance for a fail.txt file."""
# # #     while True:
# # #         result = subprocess.run(["vastai", "copy", f"{instance_id}:/root/.choline/failed.txt", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # #         if result.returncode == 0:
# # #             print(f"Failure detected on instance {instance_id}. Shutting down...")
# # #             subprocess.run(["vastai", "destroy", "instance", instance_id])
# # #             return
# # #         time.sleep(30)  # Check every 30 seconds

# # # def main():
# # #     max_price = float(input("Enter the maximum hourly price you are willing to pay: "))

# # #     instance_generator = launch.main(max_price=max_price)
# # #     try:
# # #         instance_id = next(instance_generator)
# # #         print(f"Instance ID: {instance_id}")
# # #         # monitor_instance(instance_id)
# # #     except StopIteration:
# # #         print("No instance ID was generated.")

# # # def run():
# # #     main()

# # # from . import launch  # Relative import
# # # import subprocess
# # # import time

# # # def check_for_fail_txt(vastai_id):
# # #     try:
# # #         # Execute the command to list files in the /root/.choline/ directory
# # #         command = f"vastai execute {vastai_id} 'ls -l /root/.choline/'"
# # #         result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
# # #         # Check the output directly, without trying to parse as JSON
# # #         if result.returncode == 0:
# # #             output = result.stdout.strip()
# # #             # Check if 'failed.txt' is listed in the output
# # #             if 'failed.txt' in output:
# # #                 print(f"Failure detected on Machine {vastai_id} with failed.txt present.")
# # #                 return True
# # #             else:
# # #                 print(f"failed.txt not found in /root/.choline/ on Machine {vastai_id}.")
# # #                 return False
# # #         else:
# # #             print(f"Failed to execute command on Machine {vastai_id}. Error: {result.stderr.strip()}")
# # #             return False

# # #     except Exception as e:
# # #         print(f"Exception occurred: {str(e)}")
# # #         return False

# # # def monitor_instance(instance_id):
# # #     """Monitor the instance for a fail.txt file."""
# # #     while True:
# # #         if check_for_fail_txt(instance_id):
# # #             print(f"Failure detected on instance {instance_id}. Shutting down...")
# # #             subprocess.run(["vastai", "destroy", "instance", str(instance_id)])
# # #             return
# # #         time.sleep(30)  # Check every 30 seconds

# # # def main():
# # #     max_price = float(input("Enter the maximum hourly price you are willing to pay: "))

# # #     instance_generator = launch.main(max_price=max_price)
# # #     try:
# # #         instance_id = next(instance_generator)
# # #         print(f"Instance ID: {instance_id}")
# # #         # monitor_instance(instance_id)
# # #     except StopIteration:
# # #         print("No instance ID was generated.")

# # # def run():
# # #     main()


# from . import launch  # Relative import
# import subprocess
# import time

# def check_for_fail_txt(vastai_id):
#     try:
#         # Execute the command to list files in the /root/.choline/ directory
#         command = f"vastai execute {vastai_id} 'ls -l /root/.choline/'"
#         result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
#         # Check the output directly, without trying to parse as JSON
#         if result.returncode == 0:
#             output = result.stdout.strip()
#             # Check if 'failed.txt' is listed in the output
#             if 'failed.txt' in output:
#                 print(f"Failure detected on Machine {vastai_id} with failed.txt present.")
#                 return True
#             else:
#                 print(f"failed.txt not found in /root/.choline/ on Machine {vastai_id}.")
#                 return False
#         else:
#             print(f"Failed to execute command on Machine {vastai_id}. Error: {result.stderr.strip()}")
#             return False

#     except Exception as e:
#         print(f"Exception occurred: {str(e)}")
#         return False

# def monitor_instance(instance_id):
#     """Monitor the instance for a fail.txt file."""
#     while True:
#         if check_for_fail_txt(instance_id):
#             print(f"Failure detected on instance {instance_id}. Shutting down...")
#             subprocess.run(["vastai", "destroy", "instance", str(instance_id)])
#             return
#         time.sleep(30)  # Check every 30 seconds

# def main():
#     max_price = float(input("Enter the maximum hourly price you are willing to pay: "))
#     instance_generator = launch.main(max_price=max_price)

#     for instance_id in instance_generator:
#         print(f"Instance ID: {instance_id}")
#         monitor_instance(instance_id)

# def run():
#     main()


# from . import launch  # Relative import
# import subprocess
# import time

# def check_for_fail_txt(vastai_id):
#     try:
#         # Execute the command to list files in the /root/.choline/ directory
#         command = f"vastai execute {vastai_id} 'ls -l /root/.choline/'"
#         result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
#         # Check the output directly, without trying to parse as JSON
#         if result.returncode == 0:
#             output = result.stdout.strip()
#             # Check if 'failed.txt' is listed in the output
#             if 'failed.txt' in output:
#                 print(f"Failure detected on Machine {vastai_id} with failed.txt present.")
#                 return True
#             else:
#                 print(f"failed.txt not found in /root/.choline/ on Machine {vastai_id}.")
#                 return False
#         else:
#             print(f"Failed to execute command on Machine {vastai_id}. Error: {result.stderr.strip()}")
#             return False

#     except Exception as e:
#         print(f"Exception occurred: {str(e)}")
#         return False

# def monitor_instance(instance_id):
#     """Monitor the instance for a fail.txt file."""
#     while True:
#         if check_for_fail_txt(instance_id):
#             print(f"Failure detected on instance {instance_id}. Shutting down...")
#             subprocess.run(["vastai", "destroy", "instance", str(instance_id)])
#             return
#         time.sleep(30)  # Check every 30 seconds

# failed_instances = []


# ###### t0d0 -- need to make sure setup complete within certain time frame else shutdown 
# ############### when instance is running, check for fail.txt or job_complete.txt and act acordingly



# def main():
#     max_price = float(input("Enter the maximum hourly price you are willing to pay: "))
#     print(f"Starting launch with max price: {max_price}")
#     looking_for_machine = True 

#     while looking_for_machine:
        
#         instance_generator = launch.main(max_price=max_price, exclude_instances=failed_instances)

#         for reservation_res in instance_generator:
#             print(f"Instance ID: {reservation_res}")
#             # switch instance_id
#             match reservation_res:
#                 case -1:
#                     print('failed to startup')# keep track of failed instances
#                     ins_id, con_id = reservation_res.split("_")
#                     failed_instances.append(ins_id)
#                 case 0:
#                     print("no suitable instance found")
#                     time.sleep(60)
#                     break 

#                 case _:
#                     ins_id, con_id = reservation_res.split("_")
#                     print("successfully started instance")
#                     monitor_instance(int(con_id))
        
# def run():
#     main()


from . import launch  # Relative import
import subprocess
import time

def check_for_fail_txt(vastai_id):
    try:
        # Execute the command to list files in the /root/.choline/ directory
        command = f"vastai execute {vastai_id} 'ls -l /root/.choline/'"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check the output directly, without trying to parse as JSON
        if result.returncode == 0:
            output = result.stdout.strip()
            # Check if 'failed.txt' is listed in the output
            if 'failed.txt' in output:
                print(f"Failure detected on Machine {vastai_id} with failed.txt present.")
                return True
            else:
                print(f"failed.txt not found in /root/.choline/ on Machine {vastai_id}.")
                return False
        else:
            print(f"Failed to execute command on Machine {vastai_id}. Error: {result.stderr.strip()}")
            return False

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return False

def check_for_complete_txt(vastai_id):
    try:
        # Execute the command to list files in the /root/.choline/ directory
        command = f"vastai execute {vastai_id} 'ls -l /root/.choline/'"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check the output directly, without trying to parse as JSON
        if result.returncode == 0:
            output = result.stdout.strip()
            # Check if 'job_complete.txt' is listed in the output
            if 'job_complete.txt' in output:
                print(f"Job completed on Machine {vastai_id} with job_complete.txt present.")
                return True
            else:
                print(f"job_complete.txt not found in /root/.choline/ on Machine {vastai_id}.")
                return False
        else:
            print(f"Failed to execute command on Machine {vastai_id}. Error: {result.stderr.strip()}")
            return False

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return False

def monitor_instance(instance_id, setup_timeout):
    """Monitor the instance for a fail.txt or job_complete.txt file."""
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > setup_timeout:
            print(f"Setup did not complete within {setup_timeout} seconds on instance {instance_id}. Shutting down...")
            subprocess.run(["vastai", "destroy", "instance", str(instance_id)])
            return False
        
        if check_for_fail_txt(instance_id):
            print(f"Failure detected on instance {instance_id}. Shutting down...")
            subprocess.run(["vastai", "destroy", "instance", str(instance_id)])
            return False

        if check_for_complete_txt(instance_id):
            print(f"Job completed successfully on instance {instance_id}. Shutting down...")
            subprocess.run(["vastai", "destroy", "instance", str(instance_id)])
            return True
        
        time.sleep(30)  # Check every 30 seconds

failed_instances = []

def main():
    max_price = float(input("Enter the maximum hourly price you are willing to pay: "))
    setup_timeout = int(input("Enter the maximum time (in seconds) to allow an instance to start up and install dependencies: "))
    print(f"Starting launch with max price: {max_price} and setup timeout: {setup_timeout} seconds")

    looking_for_machine = True

    while looking_for_machine:
        
        instance_generator = launch.main(max_price=max_price, exclude_instances=failed_instances)

        for reservation_res in instance_generator:
            print(f"Instance ID: {reservation_res}")
            # switch instance_id
            match reservation_res:
                case -1:
                    print('Failed to startup')
                    ins_id, con_id = reservation_res.split("_")
                    failed_instances.append(ins_id)
                case 0:
                    print("No suitable instance found")
                    time.sleep(60)
                    break 
                case _:
                    ins_id, con_id = reservation_res.split("_")
                    print("Successfully started instance")
                    job_completed = monitor_instance(int(con_id), setup_timeout)
                    if job_completed:
                        looking_for_machine = False
                    else:
                        failed_instances.append(ins_id)
                    break

def run():
    main()
