#!/usr/bin/python3

from moviepy.editor import *
import traceback
import sys
import os


path_mp4 = r'/home/andre/Videos'
path_mp3 = r'/home/andre/Music'


def download_mp3(file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            for l in lines:
                url = l.strip().replace('bttps', 'https')
                os.system(f'yt-dlp -x --audio-format mp3 -o "{path_mp3}" {url}')
    except FileNotFoundError:
        os.system(f'yt-dlp -x --audio-format mp3 -o "{path_mp3}" {file}')
    except Exception as e:
        print('Error: ',e)
        print(traceback.format_exc())
    

def download_mp4(file):
    try:
        with open(file, 'rb') as f:
            lines = f.readlines()
            for l in lines:
                url = l.strip().replace('bttps', 'https')
                os.system(f'yt-dlp -f mp4 -o "{path_mp4}" {url}')
    except FileNotFoundError:
        os.system(f'yt-dlp -f mp4 -o "{path_mp4}" {file}')
    except Exception as e:
        print('Error: ', e)
        print(traceback.format_exc())


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: ./script <link> format')
    link = sys.argv[1]
    if sys.argv[2] == 'mp3':
        file = download_mp3(link)
    elif sys.argv[2] == 'mp4':
        download_mp4(link)
