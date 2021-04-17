from pytube import YouTube
import ffmpeg

import os
import glob
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def delete_cache():
    print(bcolors.WARNING + "Removing tmp files..."  + bcolors.ENDC)

    files = glob.glob('cache/*')
    for f in files:
        os.remove(f)

    print(bcolors.OKCYAN + "Successfully removed tmp files."  + bcolors.ENDC)

def reset():
    files = glob.glob('cache/*')
    for f in files:
        os.remove(f)

    files = glob.glob('export/*')
    for f in files:
        os.remove(f)

    print(bcolors.OKCYAN + "Successfully removed files."  + bcolors.ENDC)

def main():
    #reset()

    file1 = open('links.txt', 'r', encoding="utf8")
    Lines = file1.readlines()
    
    for i in range(len(Lines)):
        video = YouTube(Lines[i].split(" ")[0])
        theme = Lines[i].split(" ", 1)[1].split("\n")[0]

        try:
            vid = video.streams.filter(file_extension='mp4').order_by('resolution')[-1].download("./cache")
            audio = video.streams.filter(only_audio=True).order_by('abr')[-1].download("./cache")

            v = ffmpeg.input("cache/" + video.title + ".mp4")
            a = ffmpeg.input("cache/" + video.title + ".webm")

            print(bcolors.WARNING + video.title + " downloading..."  + bcolors.ENDC)

            ffmpeg.output(v, a, "export/" + theme + ".mp4", loglevel="quiet").run()
            print(bcolors.OKGREEN + video.title + " downloaded successfully."  + bcolors.ENDC)
        except Exception as e:
            print("rossz videó: " + theme + str(e))

        delete_cache()
        time.sleep(20)

main()

# TO-DO: 
# 1. install this package
# 2. install python 3.9.2 with PATH
# 3. install ffmpeg (https://www.wikihow.com/Install-FFmpeg-on-Windows)
# 4. install pip packages: ffmpeg-python, git+https://github.com/pytube/pytube
# 5. edit links.txt as needed