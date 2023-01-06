#!/bin/bash

# Create an empty list of files
files=""

# Find the highest number in the list of MP3 files
max_number=0
for file in output/audio/*.mp3; do
    # Extract the number from the file name
    number=$(echo "$file" | sed -E 's/.*\/([0-9]+)\.mp3/\1/')

    # Update the maximum number if necessary
    if [ "$number" -gt "$max_number" ]; then
        max_number=$number
    fi
done

# Iterate over the numbers from 1 to the maximum number
for ((i=1; i<=$max_number; i++)); do
    # Add the file to the list
    files="$files|output/audio/$i.mp3"
done

# Remove the leading "|" from the list of files
files=${files:1}

# Merge the MP3 files using FFmpeg
ffmpeg -y -i "concat:$files" -c copy output/one_audio.mp3
