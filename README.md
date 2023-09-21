# YoutubeDownloader by using Pytube for only one video from a playlist or a single video 
**single Video**
This Python script utilizes the Pytube library _to download videos_ from a _YouTube._

**Playlist**
This Python script utilizes the Pytube library _to download videos_ from a _YouTube playlist._

**Prerequisites**
Python installed on your system.
The following Python package needs to be installed:
_Pytube_

**Usage**
-Install the required package using pip:
_pip install pytube_
-Open the Python script and replace the playlist URL with the actual YouTube playlist URL you want to download.

-Then the script will download all the videos from the specified YouTube playlist.

**Notes**
for playlist Adjust the download  _(video.streams.first().download()) _to customize the video quality or format you want to download.
for single video Adjust the download  _(video.streams[index].download()) _to customize the video quality or format you want to download.
