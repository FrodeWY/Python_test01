from io import StringIO


# 很多时候，数据读写不一定是文件，也可以在内存中读写。
# StringIO顾名思义就是在内存中读写str。
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
# 写入：
def stringio01():
    f = StringIO()
    f.write('hello\nworld')
    print(f.getvalue())  # getvalue()方法用于获得写入后的str。


# 读取：
def stringio02():
    f = StringIO('Hello\nHi\nGoodBye')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())


if __name__ == '__main__':
    # stringio01()
    stringio02()
