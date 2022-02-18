import file_path_adder
import internet
from keyboard import wait,is_pressed
from pywhatkit import playonyt
import pafy
import vlc

Instance = vlc.Instance()
player = Instance.media_player_new()

while not is_pressed("esc"):
   song = input("Video title : ")
   if song.isspace() or song=="":
      print("..............Invalid title...............\n\n\n")
      continue

   url = playonyt(song,open_video = False)
   #print("...getting url...")
   print("url : ",url)
   video_data = pafy.new(url)
   #print("...getting media...")
   audio = video_data.getbestaudio()
   stream_url = audio.url
   media = Instance.media_new(stream_url)
   #media.get_mrl()
   player.set_media(media)
   print("...Playing media...")
   player.play()
   wait("ctrl+space")
   player.stop()
   print("\n\n")
   