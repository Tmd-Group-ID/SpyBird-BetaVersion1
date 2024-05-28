import os
import time


print("Start Install Sherlock\n")
os.system('pip install sherlock-project')

for i in range(10):
    print("Process instal.........")
    time.sleep(30)

print("Finish Install")


with open("target_username.txt", "r") as f:
    usernames = [line.strip() for line in f.readlines()]


for username in usernames:
    print(f"Start Sherlock for {username}\n")
    os.system('sherlock ' + username)
