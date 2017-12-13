# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
# w, wb 文件存在则覆盖，文件不存在则创建，内容不追加
import shutil


def write01():
    with open('../resource/write.txt', 'w', encoding='utf-8') as w:
        w.write('hello world')


# a 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，
# 新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，
# 新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

def write02():
    with open('../resource/write.txt', 'a', encoding='utf-8') as w:
        w.write('Let\'s go')


def copy():
    try:
        r = open('../resource/exception.log', 'r', encoding='utf-8')
        # print(r.readlines()[0])
        w = open('../resource/write.txt', 'a', encoding='utf-8')
        rs = r.readlines()
        r.seek(
            0)  # 当我们执行完r.read(）或r.readlines()之后再执行r.read(),r.readlines()会发现没有内容展现出来，那是因为我们读取文件之后，文件指针跑到末尾了，要是想重新能够读取内容，可以执行f.seek(0),把文件指针放到起始位置
        rs2 = r.readlines()
        for val in range(len(rs)):
            w.write(rs[val])
        for val in rs2:
            w.write('rs2_____:' + val)
    except IOError as e:
        raise e
    finally:
        if r:
            r.close()
        if w:
            w.close()
    # for index, val in enumerate(r.readlines()):
    #    w.write(val)


def copy2():
    try:
        r = open('../resource/1.jpg', 'rb')
        # print(r.readlines()[0])
        w = open('../resource/2.jpg', 'wb')
        rs = r.readlines()
        for val in range(len(rs)):
            w.write(rs[val])
    except IOError as e:
        raise e
    finally:
        if r:
            r.close()
        if w:
            w.close()

def copy3():
    # shutil模块提供了copyfile()的函数,复制文件
    shutil.copyfile('../resource/1.jpg','../resource/3.jpg')


if __name__ == '__main__':
    # write01()
    # write02()
    copy()
    # copy2()
    # copy3()