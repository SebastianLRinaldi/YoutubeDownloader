from pytube import YouTube
from pytube import Playlist
from pydub import AudioSegment
from mutagen import File
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
import os

# os.system('cls')
# 
# For getting Streams and getting a Regex error pytube v15.0.0
# 6/24/23
# https://github.com/pytube/pytube/issues/1678#issuecomment-1603948730
# 

def single_url_to_yt_object(url):
    try: 
        yt_object = YouTube(url) #.bypass_age_gate()
        print("Grabbed the YouTube Object")
        return yt_object
    except(Exception) as e:
        print(f'Error with loading yt_object: {e}')
    finally:
        print("...\n")


def get_all_streams(yt_object):
    all_streams = yt_object.streams
    return all_streams

def get_all_audio_streams(yt_object):
    try:
        # yt_streams = yt_object_to_download.streams #.get_highest_resolution()
        audio_only_streams = yt_object.streams.filter(only_audio=True).desc()
        # yt_streams = yt_object_to_download.streams.filter(only_audio=True, abr="160kbps").desc()
        return audio_only_streams
    
    except(Exception) as e:
        print(f'Error with yt_object streams: {e}')

def print_all_audio_streams_from_url(url):
    yt_object = single_url_to_yt_object(url)
    audio_only_streams = get_all_audio_streams(yt_object)
    for stream in audio_only_streams:
        print(stream)

def print_all_streams_from_url(url):
    yt_object = single_url_to_yt_object(url)
    all_streams = get_all_streams(yt_object)
    for stream in all_streams:
        print(stream)

def check_mp3_properties(file_path):
    audio = File(file_path)
    if audio is not None and audio.mime[0] == "audio/mpeg" and "MPEG 1 Layer 3" in audio.pprint():
        print("MP3 compatible")
        return True
    return False


def stream_download(stream, file_name=None):
    thumb_drive_path = 'F:\\NEWMUSICDUMP'
    result = None
    try: 
        if file_name is None:
            result = stream.download(output_path=thumb_drive_path)
        elif file_name is not None:
            result = stream.download(output_path=thumb_drive_path, file_name=file_name)
        print("Download Stream Complete\n")
        return result
    except(Exception) as e:
        print(f'Error with stream_download: {e}')
    finally:
        print("...\n")

def convert_to_mp3(stream, yt_object):
    out_file = stream_download(stream)

    itag = stream.itag
    bitrate = stream.abr
    yt_title = yt_object.title
    # File type can also be gotten from the ext split tex
    # File type returns "txt", ext returns ".txt"
    file_type = stream.mime_type.split("/")[-1]

    # save the file
    full_path, ext = os.path.splitext(out_file)
    parent_dir = os.path.dirname(full_path)
    base = os.path.basename(full_path)
    new_base_name = f"{itag}-{file_type}-{bitrate}-{base}"

    new_file_name = f"{new_base_name}-Converted.mp3"
    new_file_path = os.path.join(parent_dir, new_file_name)

    # old_file_type_new_name = f"{new_base_name}.{file_type}"

    # if os.path.exists(out_file):
    #     os.rename(out_file, new_file_path)
    #     check_mp3_properties(new_file_path)
    #     full_file_name = os.path.basename(new_file_path)
    #     print(f"\nFull File Name: {full_file_name}")
    # else:
    #     print(f"File not found: {out_file}")
    
    # video = pafy.new(out_file)
    # audio = video.getbestaudio()
    # audio.download(filepath=new_file_path)
    
    

    # if os.path.exists(new_file_path):
    #     # Convert the downloaded file to MP3
    #     audio = AudioSegment.from_file(new_file_path, "mp3")
    #     audio.export(new_file_path, format="mp3")

    #     # Remove the original downloaded file
    #     os.remove(new_file_path)

    #     # Rename the converted file
    #     full_file_name = os.path.basename(new_file_path)
    #     print(f"\nFull File Name: {full_file_name}")
    # else:
    #     print(f"File not found: {out_file}")
def get_stream_from_itag22(yt_object):
    try:    
        # add in checks to see if higher version exist
        yt_stream = yt_object.streams.get_by_itag(22)
        return yt_stream

    except(Exception) as e:
        # raise Exception ("THERE WAS AN ERROR HERE!")
        print(f'Error with getting highest audio stream: {e}')

def single_videoURL_audio_only_stream_Download(url):
    yt_object = single_url_to_yt_object(url)
    streams = get_all_streams(yt_object)
    for stream in streams:
        convert_to_mp3(stream, yt_object=yt_object)
    print("\nDone Downloading all audio Streams")


# user = "https://www.youtube.com/watch?v=tBHzkpoFl2c"
# video = pafy.new(user)
# audio = video.getbestaudio()


def download_youtube_video_as_webm(youtube_url, output_dir):
    yt = YouTube(youtube_url)
    print("---webm Download---")

    # video = yt.streams.filter(only_audio=True).desc().first()
    video = yt.streams.get_by_itag(251)
    downloaded_file = video.download(output_path=output_dir)
    
    base, ext = os.path.splitext(downloaded_file)
    new_file = base + '.mp3'
    
    itag = video.itag
    bitrate = video.abr
    yt_title = yt.title
    print(f"{itag} - {bitrate} - {yt_title}")
    print("Done")

def download_youtube_video_as_mp4(youtube_url, output_dir):
    yt = YouTube(youtube_url)
    print("---")

    # video = yt.streams.filter(only_audio=True).desc().first()
    video = yt.streams.get_by_itag(22)
    downloaded_file = video.download(output_path=output_dir)
    
    base, ext = os.path.splitext(downloaded_file)
    new_file = base + '.mp3'
    
    # os.system(f'ffmpeg -i "{downloaded_file}" "{new_file}"')
    # os.remove(downloaded_file)
    itag = video.itag
    bitrate = video.abr
    yt_title = yt.title
    print(f"{itag} - {bitrate} - {yt_title}")
    print("Done")

def convert_mp4_to_mp3(mp4_file, mp3_file):
    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file, bitrate="192k")
    audioclip.close()
    videoclip.close()

def convert_webm_to_mp3(webm_file, mp3_file):
    audio_clip = AudioFileClip(webm_file)
    audio_clip.write_audiofile(mp3_file, bitrate="160k")
    audio_clip.close()

youtube_url = "https://www.youtube.com/watch?v=5gZdTZa8bOw"
output_dir = 'F:\\NEWMUSICDUMP'


download_youtube_video_as_mp4(youtube_url, output_dir)

input_file = 'F:\\NEWMUSICDUMP\\Keep It Down.mp4'
output_file = 'F:\\NEWMUSICDUMP\\22-320kpbs-Keep It Down.mp3'
convert_mp4_to_mp3(input_file, output_file)

print_all_audio_streams_from_url(youtube_url)
print_all_streams_from_url(youtube_url)


# print_all_streams_from_url(youtube_url)