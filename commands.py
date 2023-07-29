import youtubeDownloaderFunctions as YTD
import commandFunctionsHandler as commandHelper

# This is the dictionary that maps commands to functions, descriptions, and parameters
functions = {

    'MP': {
        'function': YTD.download_multiple_playlists, 
        'description': "This function downloads multiple playlists",
        'default parameters': ['None'],
        'needed parameters': ['While Loop -will need to type multiple playlist urls']
    },
    'SP': {
        'function': YTD.download_playlist_webm_to_mp3, 
        'description': "This function downloads a single playlist",
        'default parameters': ['None'],
        'needed parameters': ['single playlist url']
    },
    'S': {
        'function': YTD.single_videoURL_webm_to_mp3_stream_Download, 
        'description': "This function downloads a single video",
        'default parameters': ['None'],
        'needed parameters': ['single video url', "two commands", "three commands"]
    },

    'TXT2URL': {
        'function': YTD.download_and_convert_urls_from_txt,
        'description': "This function downloads and converts URLs from a text file",
        'default parameters': ['txt_file'],
        'needed parameters': ['txt_file - path to the text file containing the URLs']
    },

    'HELP': {
        'function': commandHelper.print_function_descriptions,
        'description': 'This function provides help information',
        'default parameters': ['None'],
        'needed parameters': []
    }
}
