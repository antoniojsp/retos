#!/bin/bash

# Function to display error messages
display_error() {
    echo "Error: $1"
    exit 1
}

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to get the operating system
get_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "macos"
    elif [[ "$OSTYPE" == "win32" ]]; then
        echo "windows"
    else
        display_error "Unsupported operating system"
    fi
}

# Function to install a package
install_package() {
    os=$(get_os)
    if [[ "$os" == "linux" ]]; then
        sudo apt-get install -y "$1"
    elif [[ "$os" == "macos" ]]; then
        brew install "$1"
    elif [[ "$os" == "windows" ]]; then
        echo "Please install $1 manually"
        exit 1
    else
        display_error "Unsupported operating system"
    fi
}

# Function to create a new virtualenv environment
create_virtualenv() {
    if ! command_exists virtualenv; then
        install_package virtualenv
    fi
    virtualenv env
    source env/bin/activate
    if [ -f requirements.txt ]; then
        pip install -r requirements.txt
    fi
    python --version
    pip freeze
}

# Function to create a new pipenv environment
create_pipenv() {
    if ! command_exists pipenv; then
        install_package pipenv
    fi
    pipenv --python 3
    if [ -f requirements.txt ]; then
        pipenv install -r requirements.txt
    fi
    pipenv --versions
    pipenv lock -r
}

# Function to create a new conda environment
create_conda() {
    if ! command_exists conda; then
        install_package conda
    fi
    conda create --name env python=3
    conda activate env
    if [ -f requirements.txt ]; then
        conda install --file requirements.txt
    fi
    conda list
}

# Check if a Python environment is active
if [ -n "$VIRTUAL_ENV" ]; then
    echo "Virtualenv environment detected"
    echo "Python version: $(python --version)"
    pip freeze
elif [ -n "$PIPENV_ACTIVE" ]; then
    echo "Pipenv environment detected"
    pipenv --versions
    pipenv lock -r
elif [ -n "$CONDA_PREFIX" ]; then
    echo "Conda environment detected"
    conda list
else
    echo "No Python environment detected"
    echo "Please select an environment to create:"
    echo "1. Virtualenv"
    echo "2. Pipenv"
    echo "3. Conda"
    read -r choice
    case $choice in
        1)
            create_virtualenv
            ;;
        2)
            create_pipenv
            ;;
        3)
            create_conda
            ;;
        *)
            display_error "Invalid choice"
            ;;
    esac
fi