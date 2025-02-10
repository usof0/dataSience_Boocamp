import os
import sys
import subprocess
import shutil

def check_venv():
    if os.environ['VIRTUAL_ENV'][-8:] != 'usof':
        raise Exception("This script must be run inside 'usof' virtual environment.")
    
def install_libraries():
    if not os.path.exists('requirements.txt'):
        raise FileNotFoundError("requirements.txt not found.")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def list_installed_libraries():
    result = subprocess.run([sys.executable, "-m", "pip", "freeze"], capture_output=True, text=True)
    installed_libraries = result.stdout.strip().split('\n')
    for library in installed_libraries:
        print(library)
    
    with open('requirements.txt', 'w') as f:
        f.write(result.stdout)

def archive_venv():
    venv_path = os.path.dirname(os.path.dirname(sys.executable))
    archive_name = "usof"
    shutil.make_archive(archive_name, 'zip', venv_path)
    
def main():
    try:
        check_venv()
        print("Running in the correct virtual environment.")

        print("Installing libraries from requirements.txt...")
        install_libraries()
        
        list_installed_libraries()

        print("\nArchiving virtual environment...")
        archive_venv()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()