import subprocess, os, tracemalloc
def libinstall(to_install:str):
    subprocess.run('pip install --upgrade pip')
    sub = subprocess.run(f'pip install {to_install}')
    if sub.returncode == 1:
        print("ERROR: Check the module name or your internet connection.")
    elif sub.returncode == 0:
        print(f"Installed {to_install}")

def geturl():
    return os.getcwd().split('kaz-ai')[0].replace('\\\\', '/')

