import os

class SpyBird:

    @staticmethod
    def show_banner():
        print("-----------------------------------------------------------------------------------------\n")
        print("SpyBird")
        print("Tool OSINT (INFORMATION GATHERING) Email and Social Media")
        print("16 May 2024")
        print("Version: 1.0.0")
        print("-----------------------------------------------------------------------------------------\n")

    @staticmethod
    def run_spybird_env():
        os.system('python spybird_env.py')

    @staticmethod
    def run_spybird_email():
        try:
            os.system('pip install socialscan')
            print("Successful install socialscan")
        except Exception as e:
            print("Error installing socialscan:", e)
        os.system('python spybird_email.py')

    @staticmethod
    def run_spybird_instagram():
        print("Start Install holehe, trio, and httpx\n")
        try:
            os.system('pip install holehe')
            os.system('pip install trio')
            os.system('pip install httpx')
            print("Successful install holehe, trio, and httpx")
        except Exception as e:
            print("Error installing library:", e)
        os.system('python spybird_instagram.py')

    @staticmethod
    def run_spybird_username_socmed():
        os.system('python spybird_username_socmed.py')

    @staticmethod
    def menu():
        print("Menu SpyBird:")
        print()
        print("1. OSINT EMAIL")
        print("2. OSINT INSTAGRAM")
        print("3. OSINT USERNAME SOCIAL MEDIA")


spybird = SpyBird()

spybird.show_banner()
spybird.run_spybird_env()

spybird.menu()

try:
    ch = int(input("Choose number menu 1-3: "))
except ValueError:
    print("Invalid input. Please enter a number between 1 and 3.")
    ch = 0

if ch == 1:
    spybird.run_spybird_email()
elif ch == 2:
    spybird.run_spybird_instagram()
elif ch == 3:
    spybird.run_spybird_username_socmed()
else:
    print("Number of menu not found")
    print("Try again")

spybird.menu()
