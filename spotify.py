import os
import spotdl
os.system('cls')

song_url = "https://open.spotify.com/track/60JiVnxyHNQPyuX5luoDZ1"  # replace with your song's URL
output_dir = "E:\344 School Python\personalProjects\Youtube Downloader\YoutubeDownloader\spotify.py"  


# settings = {
#     'output_file': 'song.mp3',
#     'output_ext': 'mp3'
# }

settings = {}
downloader = spotdl.Downloader(song_url, settings)
downloader.download()