# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。

def read(size=None):
    try:
        r = open("../resource/exception.log", 'r', encoding="utf-8")
        if size == None:
            print(r.read())
        else:
            print(r.read(size))

    except IOError as e:
        raise e
    finally:
        if r:
            r.close()


def read2():
    try:
        r = open("../resource/exception.log", 'r', encoding="utf-8")
        while r.read(100) != '':
            print(r.read(100))
    except IOError as e:
        raise e
    finally:
        r.close()


def read3():
    # Python引入了with语句来自动帮我们调用close()方法
    with open("../resource/exception.log", 'r') as f:
        print(f.read())


def read4():
    with  open("../resource/exception.log", 'r') as r:
        for index, value in enumerate(r.readlines()):
            print('第%d行，value:%s' % (index + 1, value.strip()))  # 把末尾的'\n'删掉


read4()
r = open("../resource/exception.log", 'r')
print(r.readlines()[5])  # 访问第6行
