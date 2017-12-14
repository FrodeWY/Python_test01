import base64


# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
# Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。

# 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
def base64_1():
    base__encode = base64.b64encode(b'abcd')
    print(base__encode)


# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
def base64_2():
    b_encode = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
    print(b_encode)
    urlsafe_b_decode = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
    print(urlsafe_b_decode)
    base__urlsafe_b_decode = base64.urlsafe_b64decode(b'abcd--__')
    print(base__urlsafe_b_decode)


def base64_3():
    b_encode = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
    print(b_encode)
    bd = base64.b64decode(b_encode)
    print(bd)
    print(bd.decode('utf-8'))
    b_decode = base64.b64decode(b_encode).decode('utf-8')
    print(b_decode)


def base64_4():
    s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
    print(s)
    d = base64.urlsafe_b64decode(s).decode('utf-8')
    print(d)


if __name__ == '__main__':
    # base64_1()
    # base64_2()
    base64_3()
    base64_4()
