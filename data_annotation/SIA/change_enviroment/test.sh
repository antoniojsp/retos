#!/bin/bash

# Define a function to check if a command is available
is_command_available() {
    command -v "$1" &> /dev/null
}

# Define a function to detect the Python environment
detect_environment() {
    if [ -d "venv" ]; then
        echo "virtualenv"
    elif [ -f "Pipfile" ]; then
        echo "pipenv"
    elif [ -d "env" ] && [ -f "environment.yml" ]; then
        echo "conda"
    else
        echo "none"
    fi
}

# Define a function to display environment details
display_environment_details() {
    case "$1" in
        virtualenv)
            source venv/bin/activate
            echo "Python version: $(python --version)"
            echo "Installed packages:"
            pip freeze
            ;;
        pipenv)
            echo "Python version: $(pipenv --py)"
            echo "Installed packages:"
            pipenv lock -r
            ;;
        conda)
            source env/bin/activate
            echo "Python version: $(python --version)"
            echo "Installed packages:"
            conda list
            ;;
    esac
}

# Define a function to install the environment management tool
install_tool() {
    case "$1" in
        virtualenv)
            if ! is_command_available virtualenv; then
                pip install virtualenv
            fi
            ;;
        pipenv)
            if ! is_command_available pipenv; then
                pip install pipenv
            fi
            ;;
        conda)
            if ! is_command_available conda; then
                echo "Please install Miniconda or Anaconda manually."
                exit 1
            fi
            ;;
    esac
}

# Define a function to create a new environment
create_environment() {
    case "$1" in
        virtualenv)
            virtualenv venv
            ;;
        pipenv)
            pipenv --python 3
            ;;
        conda)
            conda create --name env python=3 -y
            ;;
    esac
}

# Define a function to install packages from requirements.txt
install_packages() {
    case "$1" in
        virtualenv)
            source venv/bin/activate
            pip install -r requirements.txt
            ;;
        pipenv)
            pipenv install -r requirements.txt
            ;;
        conda)
            source env/bin/activate
            conda install --file requirements.txt -y
            ;;
    esac
}

# Main script
environment=$(detect_environment)
if [ "$environment" != "none" ]; then
    echo "Detected $environment environment."
    display_environment_details "$environment"
else
    echo "No Python environment detected."
    echo "Select an environment management tool:"
    echo "1. virtualenv"
    echo "2. pipenv"
    echo "3. conda"
    read -p "Enter your choice (1/2/3): " choice
    case "$choice" in
        1)
            environment="virtualenv"
            ;;
        2)
            environment="pipenv"
            ;;
        3)
            environment="conda"
            ;;
        *)
            echo "Invalid choice."
            exit 1
            ;;
    esac
    install_tool "$environment"
    create_environment "$environment"
    if [ -f "requirements.txt" ]; then
        install_packages "$environment"
    fi
fi