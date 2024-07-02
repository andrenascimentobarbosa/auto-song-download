#!/usr/bin/python3

import os
import sys
from pytube import YouTube
from pydub import AudioSegment


def donwload_video(youtube_link, output_folder='songs'):
    try:
        # Created output folder in it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Download the video
        yt = YouTube(youtube_link)
        video_stream = yt.streams.filter(only_audio=True).first()
        video_path = video_stream.download(output_folder)

        # Convert video to mp3
        base, ext = os.path.splitext(video_path)
        mp3_path = base + '.mp3'

        # Use pydub to convert to mp3
        audio = AudioSegment.from_file(video_path)
        audio.export(mp3_path, format='mp3')
        
        # Remove the original video file
        os.remove(vide_path)

        print('Donwloaded and converted {yt.title} to mp3 successfully.')
    except Exception as e:
        print('Error:', e)


def download_videos(songlist, output_folder='songs'):
    with open(songlist, 'r') as f:
        f.readlines()
        for song in f:
            download_video(f, output_folder)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('./script.py songlist.txt')
        sys.exit(1)

    songs = sys.argv[1]
    
    download_videos(songs)
    
