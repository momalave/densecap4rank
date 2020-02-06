# Download youtube mp4 files (still testing these APIs)
# importing the module
# pip install pytube
# or pip install pytube3 --upgrade
from pytube import YouTube
import os

#where to save
SAVE_PATH = os.path.dirname(os.path.realpath(__file__))

#insert url
YouTube('https://www.youtube.com/watch?v=ZgNu77oiKo8').streams.first().download(SAVE_PATH)
