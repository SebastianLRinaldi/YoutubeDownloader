"""
Change import based on what is breaking or working
"""

# from pytube import YouTube
from pytubefix import YouTube

youtubeObject = YouTube('https://www.youtube.com/watch?v=DASMWPUFFP4')

youtubeObject = youtubeObject.streams.get_highest_resolution()

youtubeObject.download()