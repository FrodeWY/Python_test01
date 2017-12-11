import subprocess
import time
import datetime




def get_video_time(path):
    p = subprocess.Popen("ffmpeg -i " + path + " 2>&1 | grep \'Duration\' | cut -d \' \' -f 4 | sed s/,//", shell=True,
                         stdout=subprocess.PIPE)
    time_bytes = p.stdout.readline()
    time_str = str(time_bytes, 'utf-8')
    print(time_str)
    video_time = datetime.datetime.strptime(time_str[0:-4], '%H:%M:%S')
    print(video_time)
    return video_time


fileName = "/home/ligang/jenkins-workspace/12.mp4"
video_time = get_video_time(fileName)
print("video_time:", video_time)
