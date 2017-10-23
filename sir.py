import requests
from bs4 import BeautifulSoup
from pytube import YouTube

### Autor - rlfo
### Contact - luanoliveira1992@gmail.com

def get_links():
   working_path = raw_input("Report the output path: ")
   page = requests.get("http://michaelnielsen.org/blog/quantum-computing-for-the-determined/")
   soup = BeautifulSoup(page.content, 'html.parser')
   all_youtube_link = soup.select('li a')
   
   for value_in in all_youtube_link:
      if(value_in.has_attr('href')):
        if(("http://www.youtube.com/watch?" in value_in['href']) and "TEDxWaterloo video about open science" not in value_in.get_text()):
          print("Downloading the video: "+value_in.get_text()+" wait.")          
          get_video(value_in['href'],value_in.get_text(),working_path)
          
   
def get_video(ulr_video, video_name,working_path):
    yt = YouTube(ulr_video)
    yt.set_filename(video_name)
    filter_video = yt.filter('mp4')[-1]
    filter_video.download(working_path)

   
get_links()

