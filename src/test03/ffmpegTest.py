import subprocess
import time
import datetime

CMD = ['ffmpeg', '-i', '12.mp4', '2>&1', '|', 'grep', '\'Duration\'', '|', 'cut', '-d', ' ', '-f', '4', '|', 'sed',
       's/,//']
fileName = "12.mp4"
p = subprocess.Popen("ffmpeg -i " + fileName + " 2>&1 | grep \'Duration\' | cut -d \' \' -f 4 | sed s/,//", shell=True,
                     stdout=subprocess.PIPE)
timeBytes = p.stdout.readline()
print(type(timeBytes))
timeStr = str(timeBytes, 'utf-8')
print(timeStr)
times = time.strptime(timeStr, '%H:%M:%S')
datetimeA = datetime.datetime(times)
print(datetimeA)
