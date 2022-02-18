from os import system
from file_path_adder import getpth

requirements_path = getpth("Requirements")

required_modules = ["youtube_dl","Flask","requests","Pillow","pywhatkit","python-vlc"]

print("...Downloading requirements...")
print(f"Installation Path : {requirements_path}")

for module in required_modules:
    command = f"pip install --upgrade -t \"{requirements_path}\" {module}"
    print(command)
    system(command)

print("Requirements installed successfully..")
input("press enter key")
