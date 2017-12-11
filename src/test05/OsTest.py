import os

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
print(os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('APPDATA'))
# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
path = os.path.join('../resource', 'test01')
path2 = os.path.join('../resource', 'test02')
print(path)
print(path2)
if not os.path.exists(path):
    os.mkdir(path)
if not os.path.exists(path2):
    os.mkdir(path2)
os.rmdir(path2)

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
# 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
#这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
s = os.path.split('D:/Python_test01/src/test05')
print(s)
# os.path.splitext()可以直接让你得到文件扩展名
s2= os.path.splitext('D:/Python_test01/src/test05/OsTest.py')
print(s2)
# 对文件重命名:
# os.rename('../resource/rename.log','../resource/rename.txt')
if os.path.exists('../resource/rename.txt'):
    # 删掉文件:
    os.remove('../resource/rename.txt')

print(os.path.isdir('E:/software/ideaIU-2017.3.exe'))
# 列出当前目录下的所有目录
dirlist=[x for x in os.listdir('.') if os.path.isdir(x)]
# 要列出所有的.py文件
pylist = [y for y in os.listdir('.') if os.path.splitext(y)[1]=='.py' and os.path.isfile(y)]
print(dirlist)
print(pylist)
