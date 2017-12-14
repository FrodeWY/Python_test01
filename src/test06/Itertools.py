import itertools

import time


# 因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列
def count01():
    natuals = itertools.count()
    for n in natuals:
        print(n)
        time.sleep(1)


# cycle()会把传入的一个序列无限重复下去：
def cycle01():
    cc = itertools.cycle("ABC")
    for i in cc:
        print(i)
        time.sleep(1)


# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
def repeat01():
    rp = itertools.repeat('A', 3)
    for i in rp:
        print(i)
        time.sleep(1)


# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断,来截取出一个有限的序列
def takewhile01():
    natuals = itertools.count(1)
    ns = itertools.takewhile(lambda x: x * 2 < 10, natuals)
    print(list(ns))


# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
def chain01():
    chains = itertools.chain('ABC', 'XYZ')
    for i in chains:
        print(i)
        time.sleep(1)


# groupby()把迭代器中相邻的重复元素挑出来放在一起：
def groupby01():
    gb = itertools.groupby('AAABBFFCCSS')
    for key, group in gb:
        print(key, list(group))

# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，
# 这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
def groupby02():
    gb2 = itertools.groupby('AAbBccCDDAS', lambda x: x.upper())
    for key, group in gb2:
        print(key,list(group))

if __name__ == '__main__':
    # count01()
    # cycle01()
    # repeat01()
    # takewhile01()
    # chain01()
    # groupby01()
    groupby02()