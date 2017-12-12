import pickle

d = dict(name='Bob', age=12, score=98)


def dump01():
    # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件

    print(pickle.dumps(d))


def dump02():
    # 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
    f = open('../resource/pickling.txt', 'wb')
    pickle.dump(d, f)
    f.close()


# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，
# 然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
def unpickling01():
    f = open('../resource/pickling.txt', 'rb')
    # 这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
    ud = pickle.load(f)
    f.close()
    return ud


def unpickling02():
    with open('../resource/pickling.txt', 'rb') as f:
        ud = pickle.load(f)
        return ud


if __name__ == '__main__':
    dump01()
    dump02()
    ud = unpickling01()
    print(ud)
    ud2 = unpickling02()
    print(ud2)
