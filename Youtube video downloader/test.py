from pytube import YouTube
url = "https://www.youtube.com/watch?v=vEpix-BeB_8"
youtube  = YouTube(url)
video = youtube.streams.first()
video.download("C:/Users/Ritika Goyal/Desktop")