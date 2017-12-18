import chardet


# chardet这个第三方库。用来检测编码，简单易用。
def detect01():
    print(chardet.detect(b'Hello,world'))


def detect02():
    data = '离离原上草,一岁一枯荣'.encode('gbk')
    data2 = '离离原上草,一岁一枯荣'.encode('utf-8')
    data3 = '最新の主要ニュース'.encode('euc-jp')
    print('data', chardet.detect(data))
    print('data2', chardet.detect(data2))
    print('data3', chardet.detect(data3))


if __name__ == '__main__':
    # detect01()
    detect02()
