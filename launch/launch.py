import argparse
import os
import subprocess
import json
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch

def generate_onstart_script(service_name, python_version="3.8"):
    pip_deps = "transformers flask bitsandbytes scipy accelerate"
    choline_dir = os.path.expanduser("~/.choline")
    
    if not os.path.exists(choline_dir):
        os.makedirs(choline_dir)
    
    flask_script = '''from flask import Flask, request
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch

app = Flask(__name__)

model_id = "codellama/CodeLlama-34b-Instruct-hf"
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
    user_msg = data['prompt']
    system_prompt = "<<SYS>>\\nAnswer the users question\\n<</SYS>>\\n\\n"

    # Construct the prompt
    prompt = f"<s>[INST] {user_msg} [/INST]"

    # Tokenize and send to device
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

    # Generate the response
    output = model.generate(
        inputs["input_ids"],
        max_length=8000,
        do_sample=True,
        top_p=0.9,
        temperature=0.1
    )
    output = output[0].to("cpu")

    # Decode the output
    decoded_output = tokenizer.decode(output, skip_special_tokens=True)

    return decoded_output


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    '''
    
    script_content = f'''#!/bin/bash
python_version=$(python --version 2>&1 | awk '{{print $2}}')
required_version="{python_version}"
if [ "$python_version" != "$required_version" ]; then
    echo "Incorrect Python version. Installing Python {python_version}."
    apt-get update && apt-get install -y python{python_version}
fi

apt-get update && apt-get install -y vim python-pip
pip install --upgrade pip
pip install {pip_deps}

cat <<EOL > ~/choline_api.py
{flask_script}
EOL

python ~/choline_api.py &
'''
    
    script_path = os.path.join(choline_dir, f"{service_name}_onstart.sh")
    with open(script_path, 'w') as file:
        file.write(script_content)
    
    os.chmod(script_path, 0o755)
    return script_path


def search_offers(cuda_version, additional_query=""):
    # query = f"cuda_vers == {cuda_version}"
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

def create_instance(instance_id, options):
    command = ["vastai", "create", "instance", str(instance_id)] + options
    print(command)
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Error in instance creation:", result.stderr.decode())
        return None
    print(f"Instance created successfully.")



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

def pretty_print_offer(offer, index):
    print(f"########### VASTAI OFFERS {index + 1} ###########")
    print(f"Cost per hour: {offer['dph_base']}")
    print(f"Internet download speed: {offer['inet_down']}")
    print(f"Internet upload speed: {offer['inet_up']}")
    print(f"DL Performance: {offer['dlperf']}")
    print(f"Reliability: {offer['reliability2']}")
    print(f"Storage cost: {offer['storage_cost']}")
    print(f"Internet download cost: {offer['inet_down_cost']}")
    print(f"Internet upload cost: {offer['inet_up_cost']}")
    print("#######################################\n\n")

def main():
    parser = argparse.ArgumentParser(description="Choline CLI")
    subparsers = parser.add_subparsers(dest="command")

    launch_parser = subparsers.add_parser("launch", help="Launch an instance")
    launch_parser.add_argument("service", choices=["llama2code"], help="Service to launch")

    args = parser.parse_args()

    if args.command == "launch":
        if args.service == "llama2code":
            print("Searching for cheapest 3090...")
            query = "gpu_name=RTX_3090 disk_space > 120"

            offers = search_offers("12.0", query)
            exp_storage = 120
            offers = sort_offers_by_custom_criteria(offers, expected_storage_gb=exp_storage, expected_runtime_hr=2)

            if offers:
                print("Five cheapest offers:")
                for i, offer in enumerate(offers[:5]):
                    pretty_print_offer(offer, i)

                choice = int(input("Select an offer by entering its number (1-5): ")) - 1
                selected_offer = offers[choice]
                pretty_print_offer(selected_offer, choice)
                
                confirmation = input("Would you like to proceed? (y/n): ")
                if confirmation.lower() == 'y':
                    instance_id = selected_offer["id"]
                    onstart_script = generate_onstart_script("llama2code")
                    options = ["--image", "python:3.8", "--disk", "120", "--onstart", onstart_script, "--env", "-e TZ=PDT -e XNAME=XX4 -p 22:22 -p 8080:8080"]
                    create_instance(instance_id, options)
                    
                    print(f"Instance creation request complete. Now setting up your instance with id {instance_id}. Run 'choline status 'instance id'' to check the logs for your setup.")
                else:
                    print("Operation canceled.")
            else:
                print("No suitable offers found.")

if __name__ == "__main__":
    main()