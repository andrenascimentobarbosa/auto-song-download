#!/usr/bin/python3

# Usage: ./autosong.py yoursonglist.txt.
# The song list must be a list of youtube links.
# This downloads the video, convert to mp3 and remove the mp4 version.


from pytube import YouTube
from moviepy.editor import VideoFileClip
import sys
import os

path_dir = r'/home/andre/auto-song-download/src/naruto'


def convert_file(file):
    try:
        video = VideoFileClip(file)
        audio = video.audio
        file_mp3 = file.replace(' ', '_')
        file_mp3 = file.replace("'", "")
        file_mp3 = file.lower()
        file_mp3 = file.replace('mp4', 'mp3')

        # writing the audio file
        audio.write_audiofile(file_mp3)

        # closing video and audio clips
        audio.close()
        video.close()

        # remove the mp4 file
        os.remove(file)

        print(f'Converted and removed {file}')
    except Exception as e:
        print('Error:', e)


# download video
def Download(link):
    try:
        yt = YouTube(link)
        yt = yt.streams.get_highest_resolution()
        downloaded_file = yt.download(path_dir)
        convert_file(downloaded_file)
    except Exception as e:
        print('Error:', e)
    print('done.')


# read list of songs
def main(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        for l in lines:
            file = Download(l.strip())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('./script.py songlist.txt')
    else:
        songs = sys.argv[1]
        main(songs)

