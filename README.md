# Grab Shorts from Long YT Videos

I use this script personally to download multiple videos from YT, serve out the MP4s as short formats (eg. from a given time_code for 10 seconds of duration) then do the same for the audio itself. So at the end, I get 10 sec of video and audio using the grabber.py script, and I run the merge_audio_into_one.sh which generates a full MP3 with all the short audios, that I can just add to the fancy video I create from the shorts with a program.

## To run this script, you need to have...

1. Python
2. FFMPEG

## Before running the script:

1. Copy the "youtube_urls_example.txt" and rename it to "youtube_urls.txt" then edit it to add your URLs like below (line by line):

<youtube_url_1> 00:00:32
<youtube_url_2> 00:01:07

2. You better create a folder called "output", then inside that folder create the following sub_folders: audio, temp_audio, video, temp_video

The grabber.py will get this job done quickly. Then you can get the full MP3 by just running the merge_audio_into_one.sh

If you want to use the shorts_audio_merge script, do the same to get a file called "shorts_merge.txt" which will simply create the same audio merge as merge_audio_into_one.sh, but you can specify the exact files to merge.