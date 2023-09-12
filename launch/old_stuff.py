# choline.py
import argparse
from search_and_create_instance import create_instance, search_offers, onstart_script_path
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch
import os




import argparse
import os
import subprocess
import json
import sys
from build_dockerfile import create_docker_file_from_env
import time 

def convert_version_to_int(version_str):
    return int(version_str.replace('.', ''))

def sort_offers_by_driver_and_gpu(offers):

    filtered_offers = offers # user now filters using stock vast cli 
    sorted_and_filtered_offers = sorted(filtered_offers, key=lambda x: x['dph_total'])

    return sorted_and_filtered_offers


def get_local_driver_version():
    try:
        result = subprocess.run(["nvidia-smi", "--query-gpu=driver_version", "--format=csv,noheader,nounits"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result.check_returncode()
        local_driver_version = result.stdout.decode().strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("NVIDIA driver not found on this machine. Using default version.")
        local_driver_version = "525.60.11"
    return local_driver_version

def get_local_cuda_version():
    try:
        result = subprocess.run(["nvcc", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result.check_returncode()
        version_line = result.stdout.decode().split("\n")[-2]
        local_cuda_version = version_line.split(" ")[-1]
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("CUDA not found on this machine. Using version 12.0 as default.")
        local_cuda_version = '12.0'
    return local_cuda_version

def get_current_directory_size():
    total_size = 0
    for dirpath, dirnames, filenames in os.walk('.'):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return (total_size / (1024 ** 3)) + 10  # Convert to GB and add 10 GB

# 'make the requirements less dumb' - Elon 
def search_offers(cuda_version, additional_query=""):
    query = f"cuda_vers == {cuda_version}"
    
    if additional_query:
        query = f"{query} {additional_query}"

    command = ["vastai", "search", "offers", "--raw", query]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Error in search:", result.stderr.decode())
        return []

    offers = json.loads(result.stdout.decode())
    return offers


def create_instance(instance_id, options, size_gb, storage_cost):
    # can supply --image as well as storage 
    command = ["vastai", "create", "instance", str(instance_id)] + options
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Error in instance creation:", result.stderr.decode())
        return None

    upload_cost, download_cost, storage_cost_total = get_costs(size_gb, float(result.stdout.decode()['inet_up_cost']), float(result.stdout.decode()['inet_down_cost']), storage_cost)
    print(f"Instance created successfully. Upload cost for {size_gb} GB: ${upload_cost}. Download cost for {size_gb} GB: ${download_cost}. Storage cost for {size_gb} GB: ${storage_cost_total}.")

def onstart_script_path(dockerfile_path):
    script_content = f"""#!/bin/bash
    cp {dockerfile_path} /destination/path/
    apt-get update && apt-get install -y vim
    """
    script_path = "/path/to/your_script.sh"
    with open(script_path, 'w') as file:
        file.write(script_content)
    os.chmod(script_path, 0o755)  # Make the script executable
    return script_path



def deploy_llm_flask_app():
    # This function will create a Flask app that uses the LLM model
    # and save it to a Python script that will be run on instance start.
    flask_script = """from flask import Flask, request
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch

app = Flask(__name__)

model_id = "codellama/CodeLlama-34b-hf"
quantization_config = BitsAndBytesConfig(
   load_in_4bit=True,
   bnb_4bit_compute_dtype=torch.float16
)

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=quantization_config,
    device_map="auto",
)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prompt = data['prompt']
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    output = model.generate(
        inputs["input_ids"],
        max_new_tokens=200,
        do_sample=True,
        top_p=0.9,
        temperature=0.1,
    )
    output = output[0].to("cpu")
    return tokenizer.decode(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    """

    with open("/path/to/your_flask_app.py", "w") as f:
        f.write(flask_script)

def main():
    parser = argparse.ArgumentParser(description="Choline CLI")
    subparsers = parser.add_subparsers(dest="command")

    launch_parser = subparsers.add_parser("launch", help="Launch an instance")
    launch_parser.add_argument("service", choices=["llama2code"], help="Service to launch")

    args = parser.parse_args()

    if args.command == "launch":
        if args.service == "llama2code":
            print("Searching for cheapest 3090...")
            query = "type == 3090"
            offers = search_offers("12.0", query)  # Assuming CUDA 12.0

            if offers:
                print(f"Cheapest offer: {offers[0]}")
                confirmation = input("Would you like to proceed? (y/n): ")
                if confirmation.lower() == 'y':
                    docker_file_path = "/path/to/your/Dockerfile"
                    instance_id = offers[0]["id"]
                    onstart_script = onstart_script_path(docker_file_path)
                    options = ["--image", "bobsrepo/pytorch:latest", "--disk", "20", "--onstart", onstart_script]
                    create_instance(instance_id, options)

                    # Generate Flask app for LLM
                    deploy_llm_flask_app()

                    print("Instance created and Flask app deployed.")
                else:
                    print("Operation canceled.")
            else:
                print("No suitable offers found.")

if __name__ == "__main__":
    main()