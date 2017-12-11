from collections import Iterable, Iterator

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))
print('-----------------------')

#  生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(100, Iterator))
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print('-----------------------')
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))


# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# Python的for循环本质上就是通过不断调用next()函数实现的
