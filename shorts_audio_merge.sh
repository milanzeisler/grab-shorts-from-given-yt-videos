#!/bin/bash

# Create an empty list of files
files=""

# Read the file names from shorts_merge.txt
while read -r file; do
    # Add the file to the list
    files="$files|output/audio/$file"
done < shorts_merge.txt

# Remove the leading "|" from the list of files
files=${files:1}

# Merge the MP3 files using FFmpeg
ffmpeg -y -i "concat:$files" -c copy output/shorts_audio.mp3
