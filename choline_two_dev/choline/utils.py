### t0d0 
####### handle terminations mid upload ? 
########### nonblocking upload? 

import requests
import pickle
import os
import base64
import aiohttp
import asyncio
import threading

# BASE_URL = "http://35.238.138.222:8080"
BASE_URL = "http://127.0.0.1:8080"


def cholinePath(local_path, remote_path=None):
    # adjust remote path 
    if remote_path == None: 
        remote_path = local_path
    else:
        remote_path = "/root/choline" + remote_path
        
    is_remote = os.environ.get('cholineremote')
    if is_remote:
        return remote_path
    else:
        return local_path



# def upload_object(run_name, file_name, data):
#     api_key = os.environ.get("CHOLINE_API_KEY")
#     if not api_key:
#         raise ValueError("API key not found in environment variables.")

#     serialized_data = pickle.dumps(data)
#     encoded_data = base64.b64encode(serialized_data).decode()

#     response = requests.post(
#         f"{BASE_URL}/cholineUpload",
#         data={
#             'api_key': api_key,
#             'runName': run_name,
#             'fileName': file_name,
#             'data': encoded_data
#         }
#     )
#     try:
#         return response.json()
#     except ValueError:
#         return response.text


def upload_object(run_name, file_name, data, nonblocking=False):
    def upload_task():
        api_key = os.environ.get("CHOLINE_API_KEY")
        if not api_key:
            raise ValueError("API key not found in environment variables.")

        serialized_data = pickle.dumps(data)
        encoded_data = base64.b64encode(serialized_data).decode()

        response = requests.post(
            f"{BASE_URL}/cholineUpload",
            data={
                'api_key': api_key,
                'runName': run_name,
                'fileName': file_name,
                'data': encoded_data
            }
        )
        try:
            return response.json()
        except ValueError:
            return response.text

    if nonblocking:
        threading.Thread(target=upload_task).start()
    else:
        return upload_task()



# def download_object(run_name, file_name):
#     api_key = os.environ.get("CHOLINE_API_KEY")
#     if not api_key:
#         raise ValueError("API key not found in environment variables.")

#     response = requests.get(
#         f"{BASE_URL}/cholineDownload",
#         params={
#             'api_key': api_key,
#             'runName': run_name,
#             'fileName': file_name
#         }
#     )

#     response_data = response.json()
#     byte_data = base64.b64decode(response_data['data'])
#     return byte_data

def download_object(run_name, file_name, default_object=None):
    api_key = os.environ.get("CHOLINE_API_KEY")
    if not api_key:
        raise ValueError("API key not found in environment variables.")

    try:
        response = requests.get(
            f"{BASE_URL}/cholineDownload",
            params={
                'api_key': api_key,
                'runName': run_name,
                'fileName': file_name
            }
        )

        if response.status_code != 200:
            # If the response is not successful, return the default object
            print("uable to find {} in project {}. Returning original object".format(file_name, run_name))
            return default_object

        response_data = response.json()
        byte_data = base64.b64decode(response_data['data'])

        # Attempt to load the object from the downloaded data
        try:
            downloaded_object = pickle.loads(byte_data)
            
            # Check if the type of downloaded_object matches default_object
            if default_object is not None and not isinstance(downloaded_object, type(default_object)):
                # If types don't match, return the default object
                print("WARNING -> Object in DB is of different type than the object you are syncing.")
                return default_object
            
            return downloaded_object
        except Exception:
            # If there's an error in loading, return the default object
            return default_object

    except Exception as e:
        # If there's an error in fetching data, return the default object
        return default_object


# class SampleClass:
#     def __init__(self, name, age, interests):
#         self.name = name
#         self.age = age
#         self.interests = interests

#     def __eq__(self, other):
#         return self.__dict__ == other.__dict__

# def test_choline_lib():
#     run_name = "test_run"
#     file_name = "test_class_object.pkl"
#     sample_object = SampleClass("John Doe", 30, ["reading", "traveling"])
#     upload_response = upload_data(run_name, file_name, sample_object)
#     print("Upload Response:", upload_response)

#     downloaded_serialized_data = download_data(run_name, file_name)
#     downloaded_object = pickle.loads(downloaded_serialized_data)
#     print("Downloaded Data:", downloaded_object)

#     assert downloaded_object == sample_object, "Mismatch in uploaded and downloaded class objects."

#     print("Test passed. Uploaded and downloaded class objects match.")

# test_choline_lib()


import torch
import torch.nn as nn
import torch.optim as optim
import pickle

# Assuming the upload_data and download_data functions are already defined as per previous discussions

# Define a simple neural network model
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(10, 5)

    def forward(self, x):
        x = self.fc1(x)
        return x

# def test_choline_lib():
#     model = SimpleNet()
#     optimizer = optim.SGD(model.parameters(), lr=0.01)

#     run_name = "test_run"
#     model_file_name = "test_model.pkl"
#     upload_response = upload_object(run_name, model_file_name, model)
#     print("Upload Response for Model:", upload_response)

#     downloaded_model_data = download_object(run_name, model_file_name)
#     downloaded_model = pickle.loads(downloaded_model_data)
#     print(type(downloaded_model))

#     downloaded_modelo = SimpleNet()
#     downloaded_modelo = downloaded_model
#     print(type(downloaded_modelo))

#     assert all((original_param == downloaded_param).all()
#                for original_param, downloaded_param in zip(model.parameters(), downloaded_model.parameters())), \
#         "Mismatch in uploaded and downloaded model."




#     # optimizer_file_name = "test_optimizer.pkl"
#     # serialized_optimizer = pickle.dumps(optimizer)
#     # upload_response = upload_data(run_name, optimizer_file_name, serialized_optimizer)
#     # print("Upload Response for Optimizer:", upload_response)

#     # downloaded_optimizer_data = download_data(run_name, optimizer_file_name)
#     # downloaded_optimizer_state_dict = pickle.loads(downloaded_optimizer_data)
#     # downloaded_optimizer = optim.SGD(downloaded_model.parameters(), lr=0.01)
#     # downloaded_optimizer.load_state_dict(downloaded_optimizer_state_dict)

#     # assert all((original_param == downloaded_param).all()
#     #            for original_param, downloaded_param in zip(optimizer.state_dict()['param_groups'],
#     #                                                        downloaded_optimizer.state_dict()['param_groups'])), \
#     #     "Mismatch in uploaded and downloaded optimizer."

#     print("Test passed. Uploaded and downloaded model and optimizer match.")

# test_choline_lib()

