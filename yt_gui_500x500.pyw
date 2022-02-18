from file_path_adder import getpth
import internet
from tkinter import *
from tkinter import font
from tkinter.tix import Balloon,Tk
from PIL import Image, ImageTk
from io import BytesIO
from urllib.request import urlopen
from pywhatkit import playonyt
from threading import Thread
from webbrowser import open_new_tab as web
from vlc import State
from winsound import MessageBeep
import pafy
import vlc

play_btn_path = getpth("icons","play.png")
pause_btn_path = getpth("icons","pause.png")
forward_btn_path = getpth("icons","forward.png")
backward_btn_path = getpth("icons","backward.png")

class Stream:

    song_title = ""
    thumbnail = ""
    thumbnail_url = ""
    stream_url = ""
    yt_url = ""
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    status = ""

    def __init__(self,song_title,status):
        self.song_title = song_title
        self.status = status
        self.show_status("fetching url")
        self.yt_url = playonyt(self.song_title,open_video=False)
        video_data = pafy.new(self.yt_url)
        self.thumbnail_url = video_data.getbestthumb()
        audio = video_data.getbestaudio()
        self.stream_url = audio.url
        media = self.Instance.media_new(self.stream_url)
        # media.get_mrl()
        self.player.set_media(media)

    def get_thumbnail(self):
        url_request = urlopen(self.thumbnail_url).read()
        img = Image.open(BytesIO(url_request)).resize((384,216),Image.ANTIALIAS)
        self.thumbnail = ImageTk.PhotoImage(img)
        return self.thumbnail
    
    def is_playing(self):
        return self.player.is_playing()
    
    def show_status(self,msg):
        self.status.set(msg.title())

    def backward(self):
        current_time = self.player.get_time()
        current_time -= 5000
        self.player.set_time(current_time)

    def forward(self):
        current_time = self.player.get_time()
        current_time += 5000
        self.player.set_time(current_time)

    def play_on_yt(self,event):
        self.pause()
        web(current_stream.yt_url)

    def get_state(self):
        return self.player.get_state()

    def play(self):
        global playRpauseBtn
        self.show_status("playing")
        playRpauseBtn.configure(image=pause_btn_image)
        self.player.play()

    def pause(self):
        global playRpauseBtn
        if self.is_playing():
           self.player.pause()
           self.show_status("Paused")
           playRpauseBtn.configure(image=play_btn_image)

    def stop(self):
        print("Thread stopped..")
        self.player.stop()


def playRpause():
    global current_stream
    current_song = song.get().strip()

    if current_song =="":
        pass

    elif current_stream.song_title == current_song:
        if current_stream.is_playing():
            current_stream.pause()
        else:
            current_stream.play()
        
    else:
        current_stream.stop()
        current_stream = Stream(song_title=current_song,status=curr_status)
        current_stream.play()
        img = current_stream.get_thumbnail()
        thumbnail_img.configure(image = img)
        thumbnail_img.image= img


def action():
    Thread(target=playRpause).start()


def onclick(event):
   song.delete(0,END)
   show_status("Enter song or video title")
   playRpauseBtn.configure(image=play_btn_image)


def show_status(msg):
    curr_status.set(msg.title())


def is_played(root):
    if current_stream.get_state() == State.Ended:
        show_status("Enter song or video title")
        current_stream.song_title = ""
        playRpauseBtn.configure(image=play_btn_image)

    root.after(100,is_played,root)



MessageBeep(16)

root  = Tk()
root.geometry("500x500") 
root.wm_title("yT Player")
root.wm_resizable(False,False)                                                     

balloon = Balloon(root)

curr_status = StringVar()
status = Label(textvariable=curr_status,font=("",13))

current_stream =  Stream(song_title="Manogari tamil",status=curr_status)
show_status("default song is set")

default_logo = current_stream.get_thumbnail()
thumbnail_img = Label(image=default_logo,cursor="hand2") 
thumbnail_img.pack(pady=40)
thumbnail_img.bind("<Button>",current_stream.play_on_yt)                   

song = Entry(font=("",18),justify="center",width=23)
song.insert(INSERT,current_stream.song_title)
song.place(relx=0.5,rely=0.59,anchor="n")
song.bind("<Button>",func=onclick)

status.place(relx=0.5,rely=0.71,anchor="n")   

play_btn_image = ImageTk.PhotoImage(Image.open(play_btn_path).resize((45,45),Image.ANTIALIAS))
pause_btn_image = ImageTk.PhotoImage(Image.open(pause_btn_path).resize((45,45)),Image.ANTIALIAS)
forward_btn_image = ImageTk.PhotoImage(Image.open(forward_btn_path).resize((45,45)),Image.ANTIALIAS)
backward_btn_image = ImageTk.PhotoImage(Image.open(backward_btn_path).resize((45,45)),Image.ANTIALIAS)

backward_btn_left = Button(image=backward_btn_image,command=current_stream.backward,cursor="hand2")
backward_btn_left.place(relx=0.3,rely=0.81,anchor="n")

playRpauseBtn = Button(image = play_btn_image,command=action,font=("",15,font.BOLD),cursor="hand2")
playRpauseBtn.place(relx=0.5,rely=0.81,anchor="n")

forward_btn_right = Button(image=forward_btn_image,command = current_stream.forward,cursor="hand2")
forward_btn_right.place(relx=0.7,rely=0.81,anchor="n") 

balloon.bind_widget(thumbnail_img,balloonmsg="click to open the video in youtube")
balloon.bind_widget(forward_btn_right,balloonmsg="+5 sec")
balloon.bind_widget(backward_btn_left,balloonmsg="-5 sec")
balloon.bind_widget(playRpauseBtn,balloonmsg="play/pause")

root.after(100,is_played,root)
root.mainloop()