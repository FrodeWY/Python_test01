import sys

print(sys.platform)
print('共有：', len(sys.argv), "个参数")
if len(sys.argv) < 2:
    print("请使用命令行参数")
    sys.exit(1)
for i in range(len(sys.argv)):
    print('第', (i+1), "个参数为：", sys.argv[i])


