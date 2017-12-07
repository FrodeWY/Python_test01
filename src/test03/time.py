import time

print(time.time())  # 当前时间戳
print(time.localtime(time.time()))  # 转成struct_time数组
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))  # 格式化输出struct_time
print(time.ctime())  # 返回当前时间的字符串,参数默认当前时间，可以传时间戳
