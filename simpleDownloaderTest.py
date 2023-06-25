from pytube import YouTube
import os 
os.system('cls')

yt = YouTube('https://youtu.be/9bZkp7q19f0').streams.get_highest_resolution().download()

print(yt.title)



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