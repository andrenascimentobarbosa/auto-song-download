#!/usr/bin/python3

from pytube import YouTube
import sys


def Download(link):
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()
    try:
        yt.download()
    except Exception as e:
        print('Error:', e)

    print('done.')


'''
def main(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        for l in lines:
            Download(l)
'''


def main(link):
    Download(link)


if __name__ == "__main__":
    #if len(sys.argv) != 2:
        #print('./script.py songlist.txt')
    
    #songs = sys.argv[1]
    songs = 'https://youtu.be/-wZl_ZhnVg4?si=bdxI-JQQG5bI2pqT'
    main(songs)

