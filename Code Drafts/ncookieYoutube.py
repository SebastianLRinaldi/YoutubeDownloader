from pytube import YouTube
url = 'https://www.youtube.com/watch?v=yJg-Y5byMMw'
yt = YouTube(url)
streams = yt.streams.all()
nocookie_streams = [s for s in streams if 'nocookie' in s.url]
chosen_stream = nocookie_streams[0]
chosen_stream.download()