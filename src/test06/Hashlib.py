import hashlib


# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
# 摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
# 而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。
def MD501():
    hashlib_md = hashlib.md5()
    hashlib_md.update('how to use md5 in python?'.encode('utf-8'))
    print(hashlib_md.hexdigest())
    # 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
    hashlib_md2 = hashlib.md5()
    hashlib_md2.update('how to use '.encode('utf-8'))
    hashlib_md2.update('md5 in python?'.encode('utf-8'))
    print(hashlib_md2.hexdigest())


# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
def sha1():
    hashlib_sha = hashlib.sha1()
    hashlib_sha.update('how to use md5 in python?'.encode("utf-8"))
    print('SHA1:', hashlib_sha.hexdigest())


# 经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。
# 如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。
def encode_password(username, password):
    hashlib_md = hashlib.md5()
    md5_password = password + username + 'the-Salt'
    hashlib_md.update(str(md5_password).encode('utf-8'))
    print(hashlib_md.hexdigest())


if __name__ == '__main__':
    MD501()
    sha1()
    encode_password('lili', '1234')
