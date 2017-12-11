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


# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
def read2():
    try:
        r = open("../resource/exception.log", 'r', encoding="utf-8", errors='ignore')
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


# read4()
# r = open("../resource/exception.log", 'r')
# print(r.readlines()[5])  # 访问第6行

# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
def read_byte_file():
    with open("../resource/1.jpg", 'rb') as f:
        print(f.read())



if __name__ == '__main__':
    read_byte_file()
