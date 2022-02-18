from sys import path
from os import getcwd as cwd
from os.path import join


def getpth(*pth):
    return join(cwd(),*pth)


modules_path = getpth("Requirements")

path.append(cwd())
path.append(modules_path)

print("Modules Path : ",modules_path)
print("Current Working Directory :",cwd())


