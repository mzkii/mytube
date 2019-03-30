# -*- coding: utf-8 -*-
import sys
from pytube import YouTube


def download(url):
    video = YouTube(url)
    for itag_list in video.streams.all():
        print(itag_list)
    stream = video.streams.get_by_itag(160)
    print("Downloading...")
    stream.download()
    print("DONE!")


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("ArgumentLengthError!")
        quit()
    download(sys.argv[1])
