# YoutubeDownloader
Youtube downloader for used in terminal in a ide, will add GUI at some point



If you get an error about get_throttling_function_name
Need to add this into the cipher.py in pytube v15.0.0
https://github.com/pytube/pytube/issues/1678
Added this on Augest 2nd, 2024 (working downloader)

'''
r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
'''