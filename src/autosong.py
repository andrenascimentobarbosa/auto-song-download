#!/usr/bin/python3

# Usage: ./autosong.py yoursonglist.txt.
# The song list must be a list of youtube links.
# This downloads the video, convert to mp3 and remove the mp4 version.

# Version 3.0


from pytube import YouTube
from moviepy.editor import VideoFileClip
import sys
import os


# path to the download
path_dir_songs = r'/home/andre/auto-song-download/src/songs'
path_dir_videos = r'/home/andre/auto-song-download/src/videos'


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
def Download_song(link):
    try:
        yt = YouTube(link)
        yt = yt.streams.get_highest_resolution()
        downloaded_file = yt.download(path_dir_songs)
        convert_file(downloaded_file)
    except Exception as e:
        print('Error:', e)
    print('done.')


def Download_video(link):
    try:
        yt = YouTube(link)
        yt = yt.streams.get_highest_resolution()
        downloaded_file = yt.download(path_dir_videos)
    except Exception as e:
        print('Error:', e)
    print('done.')


# read list of songs
def main_song(file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            for l in lines:
                file = Download_song(l.strip())
    except FileNotFoundError:
        Download_song(file)


def main_video(file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            for l in lines:
                file = Download_video(l.strip())
    except FileNotFoundError:
        Download_video(file)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('./script.py songlist.txt/https://youtube.com/yoursong mp3/mp4')
    else:
        if sys.argv[2] == 'mp3':
            links = sys.argv[1]
            main_song(links)
        elif sys.argv[2] == 'mp4':
            links = sys.argv[1]
            main_video(links)


