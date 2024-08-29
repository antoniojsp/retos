import subprocess

def create_venv(venv_name):
    """Creates a virtual environment using venv in macOS Zsh terminal."""
    try:
        subprocess.run(["python3", "-m", "venv", venv_name], check=True)
        print(f"Virtual environment '{venv_name}' created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment: {e}")

# Example usage:
create_venv("my_venv")