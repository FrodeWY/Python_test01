import subprocess
import time
import datetime

fileName = "/home/ligang/jenkins-workspace/12.mp4"
p = subprocess.Popen("ffmpeg -i " + fileName + " 2>&1 | grep \'Duration\' | cut -d \' \' -f 4 | sed s/,//", shell=True,
                     stdout=subprocess.PIPE)
timeBytes = p.stdout.readline()
timeStr = str(timeBytes, 'utf-8')
print(timeStr)
datetimeA = datetime.datetime.strptime(timeStr[0:-4], '%H:%M:%S')
print(datetimeA)


def get_video_time(path):
    p = subprocess.Popen("ffmpeg -i " + path + " 2>&1 | grep \'Duration\' | cut -d \' \' -f 4 | sed s/,//", shell=True,
                         stdout=subprocess.PIPE)
    time_bytes = p.stdout.readline()
    time_str = str(time_bytes, 'utf-8')
    print(time_str)
    video_time = datetime.datetime.strptime(time_str[0:-4], '%H:%M:%S')
    print(video_time)
    return video_time


video_time = get_video_time(fileName)
print("video_time:", video_time)
