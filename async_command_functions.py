import os
from pytube import YouTube, Playlist
from moviepy.editor import AudioFileClip
from concurrent.futures import ThreadPoolExecutor

def threaded_download_and_convert(url):
    # Download the video
    filepath = 'F:\\NEWMUSICDUMP'
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
    # Get the playlist
    playlist = Playlist(url)

    # Get the URLs of all videos in the playlist
    playlist_urls = playlist.video_urls

    # Download and convert all videos concurrently
    with ThreadPoolExecutor() as executor:
        # Pass the file path to download_and_convert function
        for url in playlist_urls:
            executor.submit(threaded_download_and_convert, url)




import aiohttp
import asyncio
import os
from pytube import YouTube, Playlist
from moviepy.editor import AudioFileClip

async def async_download_and_convert(session, url):
    # Download the video
    filepath = 'F:\\NEWMUSICDUMP'
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
    # Get the playlist
    playlist = Playlist(url)

    # Get the URLs of all videos in the playlist
    playlist_urls = playlist.video_urls

    # Download and convert all videos concurrently
    async with aiohttp.ClientSession() as session:
        tasks = [async_download_and_convert(session, url) for url in playlist_urls]
        await asyncio.gather(*tasks)

# async def start_download_playlist(playlist_url):
#     # Run the async function
#     asyncio.run(async_download_playlist(playlist_url))
