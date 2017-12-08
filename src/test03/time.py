import time
import datetime

print(time.time())  # 当前时间戳
print(time.localtime(time.time()))  # 转成struct_time数组
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))  # 格式化输出struct_time
print(time.ctime())  # 返回当前时间的字符串,参数默认当前时间，可以传时间戳
timestr = '00:00:47'
timestr2 = '00:01:47'
timeFormat = datetime.datetime.strptime(timestr, '%H:%M:%S')
timeFormat2 = datetime.datetime.strptime(timestr2, '%H:%M:%S')
print(timeFormat2 - timeFormat)
timestr3 = '00:00:47.42'
print(timestr3[0:-3])
# dataTimeA=datetime.datetime()
