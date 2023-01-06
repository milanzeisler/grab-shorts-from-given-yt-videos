import os
from datetime import datetime, timedelta
import threading

# Define a global counter variable
counter = 1

# Open the youtube_urls.txt file and read the URLs and start/end times
with open("youtube_urls.txt") as f:
    for line in f:
        # Split the line into URL, start time, and end time
        url, start_time = line.strip().split(" ")
        
        # Parse the start time and add 10 seconds to determine the end time
        start_time = datetime.strptime(start_time, "%H:%M:%S")
        end_time = start_time + timedelta(seconds=10)
        end_time = end_time.strftime("%H:%M:%S")
        
        # Convert start_time back to a string
        start_time = start_time.strftime("%H:%M:%S")

        # Define a function to download and process the video
        def process_video(counter, url, start_time, end_time):
            # Download the video from YouTube using youtube-dl
            os.system(f"yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' -o 'output/temp_video/{counter}.mp4' {url}")

            # Open the MP4 with FFmpeg and extract the desired part of the video
            os.system(f"ffmpeg -y -i output/temp_video/{counter}.mp4 -ss {start_time} -to {end_time} -c:v libx264 -an output/video/{counter}.mp4")
            os.system(f"ffmpeg -y -i output/temp_video/{counter}.mp4 -b:a 256k -ss {start_time} -to {end_time} -vn output/temp_audio/{counter}.mp3")
            os.system(f"ffmpeg -y -i output/temp_audio/{counter}.mp3 -b:a 256k -af afade=in:st=0:d=1,afade=out:st=9:d=1 output/audio/{counter}.mp3")

        # Create a new thread to run the function
        thread = threading.Thread(target=process_video, args=(counter, url, start_time, end_time))

        # Start the thread
        thread.start()

        # Increment the counter
        counter = counter + 1
        
    print("Finished processing videos.")
