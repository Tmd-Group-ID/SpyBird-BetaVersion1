import subprocess
import os
print("Start Create Virtual Env SpyBird\n")
os.system('python -m venv SpyBird-Env') 
print("Create Virtual Env SpyBird Success\n")

directory = 'SpyBird-Env/Scripts'
file_bat = 'activate.bat'


try:
    command = f'cd /d {directory} && {file_bat}'
    result = subprocess.run(['cmd', '/c', command], check=True, shell=True, text=True, capture_output=True)
    print("Directory Changed and Activated Virtual Env SpyBird-Env\n")
    print("Return code:", result.returncode)
    print("Output:", result.stdout)
except subprocess.CalledProcessError as e:
    print("Error during execution")
    print("Return code:", e.returncode)
    print("Output:", e.output)
    print("Error message:", e.stderr)