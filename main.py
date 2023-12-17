from pytube import *
import os 

os.system('cls')

while True:
    
    link_do_video = str(input('Link do video: '))
    yt = YouTube(link_do_video)
    print(yt.title)
    video = yt.streams.filter(file_extension='mp4')
    video = yt.streams.get_highest_resolution()
    video.download() 
    
    