
from pytubefix import YouTube
from pytubefix.cli import on_progress
 
url0 = 'https://youtu.be/NNYn8vQea14'
url1 = 'https://youtu.be/6Pti2fFwgJ0'

urls = [url0,url1]
for url in urls:
    yt = YouTube(url, on_progress_callback = on_progress)
    print(yt.title)
    
    ys = yt.streams.get_highest_resolution()
    ys.download()
