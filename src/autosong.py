#!/usr/bin/python3

from pytube import YouTube
import sys


# download video
def Download(link):
    yt = YouTube(link)
    yt = yt.streams.filter(only_audio=True).first()   # // for audio only
    #yt = yt.streams.get_highest_resolution()     // for video
    try:
        yt.download()
    except Exception as e:
        print('Error:', e)

    print('done.')


# read list of songs
def main(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        for l in lines:
            Download(l)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('./script.py songlist.txt')
    
    songs = sys.argv[1]
    main(songs)

