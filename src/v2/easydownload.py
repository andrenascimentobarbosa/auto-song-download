#!/usr/bin/python3

from moviepy.editor import VideoFileClip
import sys
import os


def download(file):
    try:
        with open(file, 'rb') as f:
            lines = f.readlines()
            for l in lines:
                os.system(f'yt-dlp {l}')
    except FileNotFoundError:
        os.system(f'yt-dlp {file}')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: ./script <link>')
    link = sys.argv[1]
    download(link)
