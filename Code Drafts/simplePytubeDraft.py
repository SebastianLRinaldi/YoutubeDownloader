# This is just a pytube test


import mutagen.id3
from pytube import YouTube
import os 
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import TextFrame, ID3NoHeaderError, ID3
import mutagen

os.system('cls')

yt = YouTube('https://youtu.be/CVDHQokn7mQ?si=FTdUqTkMSrmyJkl5').streams.get_highest_resolution().download()
# https://youtu.be/9bZkp7q19f0
print(yt.title)

# file = mutagen.File("F:\\_Small\\344 School Python\\personalProjects\\YoutubeDownloader - v2\\Cassette Insert - Sound Effect (HD).mp3").keys()
# print(file)
# audio = MP3("F:\\_Small\\344 School Python\\personalProjects\\YoutubeDownloader - v2\\Cassette Insert - Sound Effect (HD).mp3", ID3=EasyID3)
# print(EasyID3.valid_keys.keys())
# print(audio.tags)

try:
    id3v2_3 = ID3("F:\\_Small\\344 School Python\\personalProjects\\YoutubeDownloader - v2\\Cassette Insert - Sound Effect (HD).mp3", translate=False, load_v1=False)
except mutagen.id3.ID3NoHeaderError:
    # No ID3 header found; creating a new tag
    id3v2_3 = ID3()
print(id3v2_3.keys())
# comment_field = u"Your long long long comment for ID3v2.3"
# new_comment = mutagen.id3.COMM(encoding=3, desc='', text=comment_field)
# id3v2_3.add(new_comment)
v1_comment = u"Your short comment for v1"
id3v2_3["COMM"] = mutagen.id3.COMM(encoding=3, lang='eng', desc='ID3v1 Comment', text=v1_comment)
# audio.tags['mood'] = "New Artist"
# audio.tags['comments'] = 'a comment'
# Define your custom frame

# Save the changes
id3v2_3.save("F:\\_Small\\344 School Python\\personalProjects\\YoutubeDownloader - v2\\Cassette Insert - Sound Effect (HD).mp3", v2_version=3, v1=2)
# audio["title"] = "An example"
# print(audio.info.length)
# audio.save()

# # print(audio.tags.pprint())
# for tag in audio:
#     print(tag)


# from pytube import*
# import os
# os.system('cls')
# # Prompt user for YouTube URL
# url = input("Enter the URL of the YouTube video you want to download: ")

# # Create YouTube object and get the highest resolution stream
# yt = YouTube(url)
# print(yt.title)
# audio_stream = yt.streams.filter(only_audio=True).first()

# # Download video to current working directory
# print("Downloading...")
# audio_stream.download()
# print("Download complete!")