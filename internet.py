import file_path_adder
from requests import get,exceptions,Timeout
from tkinter import *
from winsound import PlaySound,SND_ASYNC

url = r"https://www.youtube.com"

print("....Waiting for network....")
try:
   get(url)
   print("...Connected to network...")

except(exceptions.ConnectionError,Timeout):
   PlaySound("SystemExit",SND_ASYNC)
   iroot = Tk()
   iroot.wm_title("yT Player")
   iroot.wm_geometry("300x100")
   Label(text="\nPlease connect to internet\nAnd try again..",font=("",15)).pack()
   iroot.wm_resizable(False,False)
   iroot.mainloop()
   exit(0)

