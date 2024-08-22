'''
NEED TO MAKE IT SO THAT A PLAYLIST GETS PUT INTO ITS OWN FOLDER
'''

'''
We only put the best, easest, quickest, streams and download processes from the command_functions here
do reuse functions from command_functions too much of a head ache (treat them as insperation for how to do it here)
'''

'''
Run in debug mode with break on errors and some maybe all the videos get a os.remove? error? 
'''

'''
Sort videos by duration, do the shortest ones first? 
Could also limit the videos that do download to only less than 20mins so if a reamdon playlist has long ones it would not do them
'''


from DownloadLocation.download_Location_Manger import *
import os
from pytube import YouTube, Playlist
from moviepy.editor import AudioFileClip
from concurrent.futures import ThreadPoolExecutor

def threaded_download_and_convert(url, filepath):
    # Download the video
    yt = YouTube(url)
    stream = yt.streams.get_by_itag(251)
    filename = stream.default_filename
    stream.download(output_path=filepath)


    # Remove the old file extension before adding the new one
    filename_without_ext, _ = os.path.splitext(filename)

    # Convert to MP3
    clip = AudioFileClip(os.path.join(filepath, filename))
    clip.write_audiofile(os.path.join(filepath, filename_without_ext + ".mp3"))

    # Delete the original video file
    os.remove(os.path.join(filepath, filename))

def threaded_download_playlist(url):
    filepath = get_default_download_location()

    # Get the playlist
    playlist = Playlist(url)

    # Get the URLs of all videos in the playlist
    playlist_urls = playlist.video_urls

    # Download and convert all videos concurrently
    with ThreadPoolExecutor(max_workers=16) as executor:
        # Pass the file path to download_and_convert function
        for url in playlist_urls:
            executor.submit(threaded_download_and_convert, url, filepath)



'''
Why am I getting the first stream instead of by itag for async
'''
import aiohttp
import asyncio
import os
from pytube import YouTube, Playlist
from moviepy.editor import AudioFileClip

async def async_download_and_convert(session, url, filepath):
    # Download the video
    yt = YouTube(url)
    stream = yt.streams.first()
    filename = stream.default_filename
    file_path = os.path.join(filepath, filename)

    # Download the video file
    async with session.get(stream.url) as response:
        with open(file_path, 'wb') as f:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                f.write(chunk)

    # Convert to MP3
    # Remove the old file extension before adding the new one
    file_path_without_ext, _ = os.path.splitext(file_path)
    clip = AudioFileClip(file_path)
    clip.write_audiofile(file_path_without_ext + ".mp3")

    # Delete the original video file
    os.remove(file_path)


async def async_download_playlist(url):
    filepath = get_default_download_location()

    # Get the playlist
    playlist = Playlist(url)

    # Get the URLs of all videos in the playlist
    playlist_urls = playlist.video_urls

    # Download and convert all videos concurrently
    async with aiohttp.ClientSession() as session:
        tasks = [async_download_and_convert(session, url, filepath) for url in playlist_urls]
        await asyncio.gather(*tasks)

# async def start_download_playlist(playlist_url):
#     # Run the async function
#     asyncio.run(async_download_playlist(playlist_url))
