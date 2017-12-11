from io import BytesIO


# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes
def bytes_io_write():
    f = BytesIO()
    f.write('中文'.encode('utf-8'))  # 请注意，写入的不是str，而是经过UTF-8编码的bytes。
    print(f.getvalue())


def bytes_io_read():
    f = BytesIO('b\xe4\xb8\xad\xe6\x96\x87')
    print(f.read())


if __name__ == '__main__':
    bytes_io_write()
