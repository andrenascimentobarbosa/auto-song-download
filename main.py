#!/usr/bin/python3

import argparse
import os
import traceback

# yt-dlp -x --audio-format mp3 -o "{path_mp3}" {file}'

# parsing arguments
parser = argparse.ArgumentParser(description="./main.py -u <url> -f <format> -p </path/to/save>")
parser.add_argument('-u', '--url', required=True, help='URL of the youtbe video')
parser.add_argument('-f', '--format', required=True, help='Format of the file')
parser.add_argument('-p', '--path', required=True, help='Path for the download')

args = parser.parse_args()

# saving arguments
url = args.url
format = args.format
path = args.path

if not os.path.exists(path):
    os.makedirs(path)

try:
    if format == 'mp3':
        os.system(f'yt-dlp -x --audio-format {format} -o "{path}/%(title)s.%(ext)s" {url}')
    elif format == 'mp4':
        os.system(f'yt-dlp -o "{path}/%(title)s.%(ext)s" {url}')
except Exception as e:
    print(f'\n\nError: {e}\n')
    print(traceback.format_exc())
    print('\n\n')



