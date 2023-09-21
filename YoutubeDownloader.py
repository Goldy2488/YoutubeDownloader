from pytube import YouTube

url="https://www.youtube.com/watch?v=OKuiyX5k6zg&t=1168s"
youtubeData = YouTube(url)

# print(youtubeData.title)
# print(youtubeData.thumbnail_url)
videos = youtubeData.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
strm = int(input("enter any stream number : "))
videos[strm].download()
print("Download is Commplete Successfully")

