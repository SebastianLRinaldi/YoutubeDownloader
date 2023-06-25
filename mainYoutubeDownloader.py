# TODO add try and excepts to all the download functions
# TODO make it download playlists 
    # Playlist titles are new folders
    
# TODO make it download music or video
# TODO make it download bulk playlists
# TODO Combine spotify and youtube playlist 

# TODO make errors red when they are printed, don't want to raise errors since we want it to just work through it
# TODO make a log system that tracks the videos downloaded and the playlist and the urls like playlistname.txt w/ then in the text file it would be yt_title - url
# TODO with the Log system make it so that the files are downloaded in a temp folder first, then when process is done, check them and then send command to move the files to the thumb drive 

# * https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/#

from pytube import YouTube
from pytube import Playlist
from pydub import AudioSegment
from mutagen import File
import os
os.system('cls')
########################################
# GETTING A YOUTUBE OBJECT FROM A SINGLE URL
########################################
def single_url_to_yt_object(url):
    try: 
        # yt_object_to_download = YouTube('https://www.youtube.com/watch?v=dINNh9Dh5Ug&t=31s') #.bypass_age_gate()
        yt_object = YouTube(url) #.bypass_age_gate()
        print("Grabbed the YouTube Object")
        return yt_object
    except(Exception) as e:
        print(f'Error with loading yt_object: {e}')
    finally:
        print("...\n")
    

########################################
# GETTING A PLAYLIST OBJECTS FROM A PLAYLIST URL
########################################
# TODO Another method that determines if the URL is a playlist or single video, sharable URLS are different
def playlist_url_to_playlist_object(url):
    try: 
        playlist_object = Playlist('https://www.youtube.com/playlist?list=PLW-S5oymMexXTgRyT3BWVt_y608nt85Uj')
        print("Grabbed the YouTube Playlist Object")
        return playlist_object
    except(Exception) as e:
        print(f'Error with loading yt_playlist_object: {e}')


###########################################
# GETTING YOUTUBE OBJECT FROM PLAYLIST OBJECT
###########################################
def playlist_object_to_yt_object(playlist_object):
    yt_objects = playlist_object.videos
    try: 
        return yt_objects
    except(Exception) as e:
            print(f'Error with getting urls from playlist object: {e}')
    finally:
        print(f'Number of youtube objects from playlist object: {len(yt_objects)}')

def playlist_object_to_url_list(playlist_object):
    return(playlist_object.video_urls)

def url_list_to_yt_objects(yt_urls):
    yt_objects = []
    for url in yt_urls:
        yt_object = single_url_to_yt_object(url)
        yt_objects.append(yt_object)
    return(yt_object)

###########################################
# GETTING STREAMS FROM YT OBJECT
###########################################
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

def get_stream_from_itag22(yt_object):
    try:    
        # add in checks to see if higher version exist
        yt_stream = yt_object.streams.get_by_itag(22)
        return yt_stream

    except(Exception) as e:
        # raise Exception ("THERE WAS AN ERROR HERE!")
        print(f'Error with getting highest audio stream: {e}')

def get_highest_audio_stream_from_itag(yt_object):
    print(yt_object)


###########################################
# PRINTING SPECIFIC STREAMS FROM YT OBJECT
###########################################
def print_all_streams_from_url(url):
    yt_object = single_url_to_yt_object(url)
    all_streams = get_all_streams(yt_object)
    for stream in all_streams:
        print(stream)

def print_all_streams_from_yt_object(yt_object):
    all_streams = get_all_streams(yt_object)
    for stream in all_streams:
        print(stream)

def print_all_audio_streams_from_url(url):
    yt_object = single_url_to_yt_object(url)
    audio_only_streams = get_all_audio_streams(yt_object)
    for stream in audio_only_streams:
        print(stream)

def print_all_audio_streams_from_yt_object(yt_object):
    audio_only_streams = get_all_audio_streams(yt_object)
    for stream in audio_only_streams:
        print(stream)

def print_all_audio_streams_from_url_short(url):
    yt_object = single_url_to_yt_object(url)
    audio_only_streams = get_all_audio_streams(yt_object)
    try:    
        for stream in audio_only_streams:
            file_type = stream.mime_type.split("/")[-1]
            bitrate = stream.abr
            print(f"ITAG: {stream.itag}, FILETYPE: {file_type}, KBPS: {bitrate}, STREAM: {stream}\n")
            
    except(Exception) as e:
        print(f'Error with finding audio stream {stream}: {e}')

def print_all_audio_streams_from_yt_object_short(yt_object):
    # Print the available mp3 version to download
    audio_only_streams = get_all_audio_streams(yt_object)
    try:    
        for stream in audio_only_streams:
            file_type = stream.mime_type.split("/")[-1]
            bitrate = stream.abr
            print(f"ITAG: {stream.itag}, FILETYPE: {file_type}, KBPS: {bitrate}, STREAM: {stream}\n")
    except(Exception) as e:
        print(f'Error with finding audio stream {stream}: {e}')

########################################
# TEST THINGS WITH YT STREAMS
########################################
def download_all_yt_audio_stream_with_itag(yt_streams):
    try:    
        for itm in yt_streams:
            print(f"{str(itm.itag)} OBJECT: {itm}\n")
            download_yt_video(itm, mp3_only=True)
    except(Exception) as e:
        print(f'Error with finding itaged audio streams: {e}')
########################################
# CHECK IF FORMAT IS MP3
########################################
def check_mp3_properties(file_path):
    audio = File(file_path)
    if audio is not None and audio.mime[0] == "audio/mpeg" and "MPEG 1 Layer 3" in audio.pprint():
        return True
    return False

########################################
# EDIT FUNCTIONS BEFORE DOWNLOADING TASK
########################################
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
    try:
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

        new_file_name = f"{new_base_name}.mp3"
        new_file_path = os.path.join(parent_dir, new_file_name)

        print(f"OUT FILE: {out_file}") # Need this
        print(f"FULL DIR PATH: {full_path}")
        print(f"PARENT DIR: {parent_dir}")
        print(f"BASE NAME: {base}")
        print(f"BASE FILE TYPE: {ext}\n")
        print(f"New File Name: {new_file_name}")
        print(f"NEW BASE NAME: {new_base_name}")
        print(f"NEW FILE PATH: {new_file_path}") # Need this
        exit()
        # ! When a file already exists it still saves it but without changing the file type

        if os.path.exists(out_file):
            os.rename(out_file, new_file_path)
            full_file_name = os.path.basename(new_file_path)
            print(f"\nFull File Name: {full_file_name}")
        else:
            print(f"File not found: {out_file}")
        # os.rename(old_file_path, new_file_path)

        # if os.path.exists(out_file):
        #     # Convert the downloaded file to MP3
        #     audio = AudioSegment.from_file(out_file, file_type)
        #     audio.export(new_file_path, format="mp3")

        #     # Remove the original downloaded file
        #     os.remove(out_file)

        #     # Rename the converted file
        #     full_file_name = os.path.basename(new_file_path)
        #     print(f"\nFull File Name: {full_file_name}")
        # else:
        #     print(f"File not found: {out_file}")

    except(Exception) as e:
        print(f'Error with edit_and_save_new_file_name: {e}')
    
    finally:
            return {'yt_title': yt_title, 
            'file_type':file_type, 
            'itag':itag, 
            'bitrate':bitrate}



########################################
# ON COMPLETE OR FAILURE
########################################
def on_complete(new_save):
    YouTubeTitle = new_save['yt_title']
    BiteRate = new_save['bitrate']
    FileType = new_save['file_type']
    Itag = new_save['itag']
    print(f"Successfully downloaded {Itag}-{BiteRate}-{YouTubeTitle} with file type {FileType} as a MP3 file!\n")


########################################
# DOWNLOADING SPECIFIC TASK
########################################
def download_yt_video(stream, yt_object=None, mp3_only=False, with_itag = False):
    try: 
        # [x] make it download to thumb drive
        # Define the file path on the thumb drive
        # file_path = os.path.join(thumb_drive_path, yt_object.title)

        # Download the video to the thumb drive
        thumb_drive_path = 'F:\\NEWMUSICDUMP'
        if yt_object is None:
            stream.download(output_path=thumb_drive_path)
            print("Default download with yt_object")

        elif yt_object is not None and with_itag is True:
            # out_file = stream.download(output_path=thumb_drive_path)
            new_save = convert_to_mp3(stream, yt_object)
            on_complete(new_save)
        elif mp3_only is True:
            # stream.download(output_path=thumb_drive_path, filename=f"item{stream.itag}.mp3")
            stream.download(output_path=thumb_drive_path, filename=f"{yt_object.title}.mp3")
            print("Downloaded with simple mp3 conversion 1: {yt_object.title}.mp3 ")

        elif yt_object is not None and mp3_only is True:
            stream.download(output_path=thumb_drive_path, filename=f"{yt_object.title}.mp3")
            print("Downloaded with simple mp3 conversion 2: {yt_object.title}.mp3 ")

        else:
            stream.download(output_path=thumb_drive_path)
            print("Else condition with Default download with yt_object")
        print("Successfully downloaded this Stream\n")
    except(Exception) as e:
        print(f'Error with downloading: {e}')
    
    finally:
        print("...\n")



########################################
# THE YOUTUBE DOWNLOADER TESTERS
########################################
def test1():

    # youtube_object = load_yt_object_by_playlist_url("")
    # get_yt_url_from_playlist_object(youtube_object)
    youtube_object = single_url_to_yt_object("https://www.youtube.com/watch?v=tBHzkpoFl2c")

    youtube_stream = get_highest_audio_stream_from_itag(youtube_object)

    download_yt_video(youtube_stream, yt_object=youtube_object, mp3_only=True)


def single_videoURL_all_stream_Download(url):
    yt_object = single_url_to_yt_object(url)
    streams = get_all_streams(yt_object)
    for stream in streams:
        download_yt_video(stream, yt_object=yt_object, with_itag=True)
    print("\nDone Downloading all Streams")

def single_videoURL_audio_only_stream_Download(url):
    yt_object = single_url_to_yt_object(url)
    streams = get_all_audio_streams(yt_object)
    for stream in streams:
        download_yt_video(stream, yt_object=yt_object, with_itag=True)
    print("\nDone Downloading all audio Streams")

########################################
# THE YOUTUBE DOWNLOADER MAIN
########################################
def main():
    # user = input("Enter URL: ")
    user = "https://www.youtube.com/watch?v=tBHzkpoFl2c"
    # print_all_streams_from_url(user)
    # print("")
    # print_all_audio_streams_from_url(user)
    # print("")
    # print_all_audio_streams_from_url_short(user)
    # single_videoURL_all_stream_Download(user)
    single_videoURL_audio_only_stream_Download(user)


main()