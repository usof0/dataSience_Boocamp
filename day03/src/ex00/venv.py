import os

def test_env():
    virtual_env = os.environ.get('VIRTUAL_ENV')
    if virtual_env:
        print(f"Your current virtual env is {virtual_env}")
    else:
        print("No virtual environment is currently active.")

if __name__ == "__main__":
    test_env()
    