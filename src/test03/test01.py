import sys
import platform

print(sys.platform)
print('共有：', len(sys.argv), "个参数")
if len(sys.argv) < 2:
    print("请使用命令行参数")
    # sys.exit(1)
for i in range(len(sys.argv)):
    print('第', (i + 1), "个参数为：", sys.argv[i])

print(sys.getdefaultencoding())
print(sys.path)
print('操作系统名称及版本号：', platform.platform())
print('操作系统类型：', platform.system())
print('python修订版本信息：',platform.python_revision())
print('python解释器实现版本信息：',platform.python_implementation())
