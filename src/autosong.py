#!/usr/bin/python3


# This script automates converting from mp4 to mp3  and downloading songs.

import sys


def main(file):
    with open(file, 'r') as f:
        songs = f.readlines()
        for song in songs:
            print(song)
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('./script songlist.txt')
        sys.exit()

    file = sys.argv[1]
    main(file)
