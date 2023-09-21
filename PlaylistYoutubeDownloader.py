from pytube import Playlist

play=Playlist("https://www.youtube.com/playlist?list=PLjVLYmrlmjGfhqSO3rF4n02rrj9w2Ch2C")
print(f'Downloading :{play.title}')

for video in play.videos:
    video.streams.first().download()

