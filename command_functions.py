# TODO add try and excepts to all the download functions
# TODO make it download playlists 
    # Playlist titles are new folders
    # Title allowed characters, make it so it keeps Case and if not allowed, make alternative character list
    
# TODO make it download music or video
# TODO make it download bulk playlists
# TODO Combine spotify and youtube playlist 

# TODO make errors red when they are printed, don't want to raise errors since we want it to just work through it
# TODO make a log system that tracks the videos downloaded and the playlist and the urls like playlistname.txt w/ then in the text file it would be yt_title - url
# TODO with the Log system make it so that the files are downloaded in a temp folder first, then when process is done, check them and then send command to move the files to the thumb drive 
# TODO Multiple load bars that show progress for each action per video, getting objects, downloading, converting..etc 
# * https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/#

from pytube import YouTube
from pytube import Playlist
from mutagen import File
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
import os

os.system('cls')

########################################
# YOUTUBE OBJECTS
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
        playlist_object = Playlist(url)
        print("Grabbed the YouTube Playlist Object")
        return playlist_object
    except(Exception) as e:
        print(f'Error with loading yt_playlist_object: {e}')


##############################################################
# GETTING MULTIPLE PLAYLIST OBJECTS FROM MULTIPLE PLAYLIST URL
##############################################################
def download_multiple_playlists():
    playlist_urls = []
    user = ""
    playlist_count = len(playlist_urls)

    print("\nType stop to start playlist downloads")
    while user != "stop":
        print("Enter URLS till you are done")
        user = input("INPUT: ")
        playlist_urls.append(user)
    
    if playlist_count < 1:
        print("NO URLS ENTERED")
    else:
        print(f"Starting download for ")
        for playlist_url in playlist_urls:
             download_playlist_webm_to_mp3(playlist_url)



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
# =====================================

def download_playlist_webm_to_mp3(url):
    # TODO Add a feature that for each playlist make a folder with the name
    # TODO To make this work will need to have a char checker and corrector like last time so files and directories can be made without issues
    # TODO Make a log system or a tracker of failed and successed downloads and at what point they failed, if we have retrys enabled then log how many attemps it tried before giving up
    # TODO On a fail or Age restricted video add a retry attempt like 10 if single or 5 if playlist idk some random number i Guess 

    # TODO Add a feature where you check the playlist title and the list of songs and the count before commiting to the download process

    # ! I am pretty sure we could cut down and go straight downloading from yt_objects instead of getting the links then to yt_objects

    playlist_object = playlist_url_to_playlist_object(url)
    playlist_urls = playlist_object_to_url_list(playlist_object)

    # ! Add in multithreading and parell processing for playlist since it can be quite large 
        # TODO Maybe throw in a estimated time for completion so we can compare when using fun computer optimzations 
        # TODO Could be throwing this in earlier than the computer processing stuff for the feature to check if we want to commit
    
    # This will be a bigger goal 

    for url in playlist_urls:
        # ! Add a counter or tracker for seeing how much is left  to download from the playlist
        single_videoURL_webm_to_mp3_stream_Download(url)
        # ! Add a end card for when you are done downloading a playlist


########################################
# YOUTUBE OBJECTS TO STREAMS
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

def get_highest_mp4_stream(yt_object):
    try:    
        # add in checks to see if higher version exist
        yt_stream = yt_object.streams.get_by_itag(22)
        return yt_stream

    except(Exception) as e:
        # raise Exception ("THERE WAS AN ERROR HERE!")
        print(f'Error with getting highest mp4  stream: {e}')

def get_highest_webm_stream(yt_object):
    try:    
        # add in checks to see if higher version exist
        yt_stream = yt_object.streams.get_by_itag(251)
        return yt_stream

    except(Exception) as e:
        # raise Exception ("THERE WAS AN ERROR HERE!")
        print(f'Error with getting highest webm stream: {e}')


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
def download_all_yt_audio_stream_by_itag(yt_streams):
    try:    
        for stream in yt_streams:
            print(f"{str(stream.itag)} OBJECT: {stream}\n")
            stream_to_a_download(stream, mp3_only=True)
    except(Exception) as e:
        print(f'Error with finding itaged audio streams: {e}')



########################################
# CHECKER IF FORMAT IS MP3
########################################
def check_mp3_properties(file_path):
    audio = File(file_path)
    if audio is not None and audio.mime[0] == "audio/mpeg" and "MPEG 1 Layer 3" in audio.pprint():
        return True
    return False
# =====================================



########################################
# CONVERTS TO FORMAT MP3
########################################
def convert_mp4_to_mp3(input_path_mp4, output_path_mp3):
    videoclip = VideoFileClip(input_path_mp4)
    audioclip = videoclip.audio
    audioclip.write_audiofile(output_path_mp3, bitrate="192k")
    audioclip.close()
    videoclip.close()

def convert_webm_to_mp3(input_path_webm, output_path_mp3):
    audio_clip = AudioFileClip(input_path_webm)
    audio_clip.write_audiofile(output_path_mp3, bitrate="160k")
    audio_clip.close()


########################################
# CONVERT FUNCTIONS FOR DOWNLOADING TASK
########################################
def convert_to_mp3(stream, yt_object):
    out_file = default_stream_download(stream)
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
        new_base_name = f"{base}-{itag}-{file_type}-{bitrate}"

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

        try: 
            if file_type == "mp4":
                convert_mp4_to_mp3(out_file, new_file_path)
            elif file_type == "webm":
                convert_webm_to_mp3(out_file, new_file_path)

            if os.path.exists(out_file):
                os.remove(out_file)
                print("base file deleted!")
            else:
                print(f"File not found: {out_file}")
            
        except(Exception) as e:
            print(f'Error stream converting or deleting downloading: {e}')

        # ! When a file already exists it still saves it but without changing the file type

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
# DOWNLOADING TASK
########################################
########################################
# STREAM DONWLOAD
########################################
def default_stream_download(stream, file_name=None):
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


def stream_to_a_download(stream, 
                         yt_object=None, 
                         mp3_only=False, 
                         ):
    try: 
        # [x] make it download to thumb drive
        # Define the file path on the thumb drive
        # file_path = os.path.join(thumb_drive_path, yt_object.title)

        # Download the video to the thumb drive

        if yt_object is None:
            default_stream_download()
            print("Default stream download")

        # elif yt_object is not None and with_itag is True:
        #     # out_file = stream.download(output_path=thumb_drive_path)
        #     new_save = convert_to_mp3(stream, yt_object)
        #     on_complete(new_save)

        elif yt_object is not None and mp3_only is True:
            # Download base file in youtubes format 
            new_save = convert_to_mp3(stream, yt_object)
            on_complete(new_save)
            

        # elif yt_object is not None and mp3_only is True:
        #     stream.download(output_path=thumb_drive_path, filename=f"{yt_object.title}.mp3")
        #     print("Downloaded with simple mp3 conversion 2: {yt_object.title}.mp3 ")

        else:
            # default_stream_download()
            print("Else condition with Default download ")
        print("Successfully downloaded this Stream\n")
    except(Exception) as e:
        print(f'Error with making a stream into a downloading: {e}')
    
    finally:
        print("...\n")




###################################################
# THE YOUTUBE DOWNLOADER FUNCTIONS BY STREAM FORMAT
###################################################
def single_videoURL_all_stream_default_type_Download(url):
    yt_object = single_url_to_yt_object(url)
    streams = get_all_streams(yt_object)
    for stream in streams:
        stream_to_a_download(stream)
    print("\nDone Downloading all Streams")

def single_videoURL_audio_only_stream_default_type_Download(url):
    yt_object = single_url_to_yt_object(url)
    streams = get_all_audio_streams(yt_object)
    for stream in streams:
        stream_to_a_download(stream)
    print("\nDone Downloading all audio Streams")


def single_videoURL_mp4_to_mp3_stream_Download(url):
    yt_object = single_url_to_yt_object(url)
    stream = get_highest_mp4_stream(yt_object)
    stream_to_a_download(stream, yt_object=yt_object, mp3_only=True)
    print("\nDone Downloading mp4 to mp3 audio Stream")

def single_videoURL_webm_to_mp3_stream_Download(url):
    print(f"THISURL: {url}")
    yt_object = single_url_to_yt_object(url)
    stream = get_highest_webm_stream(yt_object)
    stream_to_a_download(stream, yt_object=yt_object, mp3_only=True)
    print("\nDone Downloading mp4 to mp3 audio Stream")


###################################################
# Any txt file list to python list to download
###################################################
def convertTxtFile_to_URL_List(file_path):
    file_path = file_path.lstrip('\u202a')  # Remove the \u202a character from the start of the file path
    txt_file_normilzed = os.path.normpath(file_path)
    with open(txt_file_normilzed, 'r') as file:
        content = file.readlines()
    urls = [line.strip() for line in content if "https://youtube.com" in line]
    return urls


def download_and_convert_urls_from_txt(txt_file):
    converted_urls = convertTxtFile_to_URL_List(txt_file)
    for url in converted_urls:
        single_videoURL_webm_to_mp3_stream_Download(url)





















########################################
# THE YOUTUBE DOWNLOADER TESTERS
########################################
def test1():
    # youtube_object = load_yt_object_by_playlist_url("")
    # get_yt_url_from_playlist_object(youtube_object)
    youtube_object = single_url_to_yt_object("https://www.youtube.com/watch?v=tBHzkpoFl2c")

    youtube_stream = get_highest_audio_stream_from_itag(youtube_object)

    stream_to_a_download(youtube_stream, yt_object=youtube_object, mp3_only=True)



########################################
# THE YOUTUBE DOWNLOADER COMMANDS DRAFT
########################################
def startProgram():
    commands_and_uses = {
        "MP" : "Multiple Playlists Download",
        "SP" : "Single Playlist Download",
        "S" : "Single Video Download",

    }

    user = input("INPUT: ")

    while user != "EXIT":
        if user == "commands":
            print("---- Commands ----\n")
            for command in commands_and_uses:
                print(f"\tKey: {command}, Description: {commands_and_uses[command]}")
            print("---- End Commands ----\n")

        elif user == "SP":
            user = input("Enter URL: ")
            download_playlist_webm_to_mp3(user)
        
        else:
            print("INVALID COMMAND")

########################################
# THE YOUTUBE DOWNLOADER MAIN
########################################
