import subprocess
import sys

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

def get_python_version():
    return sys.version.split(' ')[0]


def get_requirements_list():
    result = subprocess.run(["pip", "freeze"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Error getting requirements. Using empty requirements.")
        return []
    req_list = result.stdout.decode().split("\n")

    # Excluding all pyobjc packages
    req_list = [req for req in req_list if "pyobjc" not in req]

    # Replacing "@ file" entries with actual versions
    for i, req in enumerate(req_list):
        if "@ file" in req:
            pkg_name = req.split(" @ ")[0]
            pkg_show_result = subprocess.run(["pip", "show", pkg_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            version_line = [line for line in pkg_show_result.stdout.decode().split("\n") if "Version:" in line][0]
            version = version_line.split(" ")[-1]
            req_list[i] = f"{pkg_name}=={version}"

    return req_list


def get_conda_version():
    result = subprocess.run(["conda", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Error getting Conda version. Using 'latest' as default.")
        return 'latest'
    conda_version = result.stdout.decode().strip().split(" ")[-1]
    return conda_version

def create_dockerfile(conda_version, req_list, cuda_version, python_version, working_dir="/choline"):
    dockerfile_lines = [
        f"FROM conda/miniconda3-cuda{cuda_version}-cudnn8-runtime:{conda_version}",
        f"ENV PYTHON_VERSION={python_version}",
        f"WORKDIR {working_dir}",
        "RUN conda install -y python=${PYTHON_VERSION}",
        "RUN conda install -y pip",
    ] + [f"RUN pip install {req}" for req in req_list]

    with open('Dockerfile', 'w') as file:
        file.write('\n'.join(dockerfile_lines))

    print(f"Dockerfile created with Conda {conda_version}, CUDA {cuda_version}, Python {python_version}, and requirements from current environment.")

# Retrieve local CUDA version
local_cuda_version = get_local_cuda_version()

# Retrieve local Python version
local_python_version = get_python_version()

# Retrieve requirements list from the current environment
req_list = get_requirements_list()

# Retrieve local Conda version
conda_version = get_conda_version()

# Create Dockerfile with the collected information
create_dockerfile(conda_version, req_list, local_cuda_version, local_python_version)
