import command_functions as CF
import multi_download_command_functions as ACF
import mapper_helpers as MH

# This is the dictionary that maps commands to functions, descriptions, and parameters
functions = {

    'TSP': {
        'function': ACF.threaded_download_playlist, 
        'description': "This function downloads a single playlist with threads - Gets some then Converts a lot at once then grabs more",
        'default parameters': ['None'],
        'needed parameters': ['single playlist url']
    },

    'ASP': {
        'function': ACF.async_download_playlist, 
        'description': "This function downloads a single playlist asynchronously - Gets all then converts one at a time",
        'default parameters': ['None'],
        'needed parameters': ['single playlist url']
    },

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

    'S': {
        'function': CF.single_videoURL_webm_to_mp3_stream_Download, 
        'description': "This function downloads a single video",
        'default parameters': ['None'],
        'needed parameters': ['single video url', "two commands", "three commands"]
    },

    'TXT2URL': {
        'function': ACF.threaded_download_list_of_urls,
        'description': "Converts URLs from a text file, downloads them via threading",
        'default parameters': ['txt_file'],
        'needed parameters': ['txt_file - path to the text file containing the URLs']
    },

    'TEST': {
        'function': CF.print_all_streams_from_url,
        'description': "Function testing if pytube libary works this doesn't download just trys to get the stream",
        'default parameters': ['None'],
        'needed parameters': ['single video url']
    },

    'HELP': {
        'function': lambda: MH.print_function_descriptions(functions),
        'description': 'This function provides help information',
        'default parameters': ['None'],
        'needed parameters': []
    }
}


'''
5. Python Files with dataclass or NamedTuple
Pros:
Use Python's native capabilities to define clear, structured data types.
Provides type safety and can include methods for data manipulation.

Cons:
Less flexible than a dictionary for dynamic configurations.
Requires Python knowledge to understand and modify.
Example:


from dataclasses import dataclass
from typing import List, Callable

@dataclass
class FunctionConfig:
    function: Callable
    description: str
    default_parameters: List[str]
    needed_parameters: List[str]

functions = {
    'TSP': FunctionConfig(
        function=ACF.threaded_download_playlist,
        description="This function downloads a single playlist with threads...",
        default_parameters=["None"],
        needed_parameters=["single playlist url"]
    ),
    ...
}
'''