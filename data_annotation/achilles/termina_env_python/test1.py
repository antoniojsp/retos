import subprocess

def create_venv(venv_name):
    """Creates a virtual environment using venv."""
    try:
        subprocess.check_call(['python3', '-m', 'venv', venv_name])
        print(f"Virtual environment '{venv_name}' created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment: {e}")

if __name__ == "__main__":
    venv_name = input("Enter the name for your virtual environment: ")
    create_venv(venv_name)