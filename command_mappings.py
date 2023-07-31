import command_functions as CF
import async_command_functions as ACF
import mapper_helpers as MH

# This is the dictionary that maps commands to functions, descriptions, and parameters
functions = {

    'MP': {
        'function': CF.download_multiple_playlists, 
        'description': "This function downloads multiple playlists",
        'default parameters': ['None'],
        'needed parameters': ['While Loop -will need to type multiple playlist urls']
    },

    'SP': {
        'function': CF.download_playlist_webm_to_mp3, 
        'description': "This function downloads a single playlist",
        'default parameters': ['None'],
        'needed parameters': ['single playlist url']
    },

    'TSP': {
        'function': ACF.threaded_download_playlist, 
        'description': "This function downloads a single playlist with threads",
        'default parameters': ['None'],
        'needed parameters': ['single playlist url']
    },

    'ASP': {
        'function': ACF.async_download_playlist, 
        'description': "This function downloads a single playlist asynchronously",
        'default parameters': ['None'],
        'needed parameters': ['single playlist url']
    },

    'S': {
        'function': CF.single_videoURL_webm_to_mp3_stream_Download, 
        'description': "This function downloads a single video",
        'default parameters': ['None'],
        'needed parameters': ['single video url', "two commands", "three commands"]
    },

    'TXT2URL': {
        'function': CF.download_and_convert_urls_from_txt,
        'description': "This function downloads and converts URLs from a text file",
        'default parameters': ['txt_file'],
        'needed parameters': ['txt_file - path to the text file containing the URLs']
    },

    'HELP': {
        'function': lambda: MH.print_function_descriptions(functions),
        'description': 'This function provides help information',
        'default parameters': ['None'],
        'needed parameters': []
    }
}
