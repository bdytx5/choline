#!/bin/bash

# Check if conda command exists
if command -v conda > /dev/null 2>&1; then
    echo "==> Detected Conda environment"
    conda list
    conda info
else
    echo "==> Conda not detected"
fi

# Check if python command exists
if command -v python > /dev/null 2>&1; then
    echo "==> Python version"
    python --version

    echo "==> Python packages (via pip freeze)"
    python -m pip freeze
else
    echo "==> Python not detected"
fi

# Check for CUDA details
if command -v nvidia-smi > /dev/null 2>&1; then
    echo "==> NVIDIA System Management Interface (CUDA details)"
    nvidia-smi
else
    echo "==> NVIDIA tools not detected"
fi
