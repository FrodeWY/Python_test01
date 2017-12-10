#  abs(-10)是函数调用，而abs是函数本身。
#  函数本身也可以赋值给变量，即：变量可以指向函数。
from functools import reduce
from operator import itemgetter

f = abs
print(f(-10))


# 函数名其实就是指向函数的变量！对于abs()这个函数，
# 完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！
# 把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数而是指向一个整数10！
# abs = 10
# abs(-10)


# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    result = f(x) + f(y)
    return result


result = add(4, -5, abs)
print(result)


# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x


iterator_f = map(f, [1, 2, 3, 4, 5])
print(list(iterator_f))
# map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数
iterator_s = map(str, [1, 2, 3, 4, 5])
print(next(iterator_s))
print(list(iterator_s))


def f2(x, y):
    return x * y


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
reduce1 = reduce(f2, [1, 2, 3, 4, 5])  # 类似求积
print(reduce1)


def f3(a, b):
    return a * 10 + b


reduce2 = reduce(f3, [1, 2, 3, 4, 5])
print(reduce2)


def f4(a):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}
    return digits[a]


print('---------------------------')
reduce3 = reduce(f3, map(f4, '12345'))
print(reduce3)


# 整合：将字符串转为数字
def str2int(s):
    def f3(a, b):
        return a * 10 + b

    def f4(a):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[a]

    return reduce(f3, map(f4, s))


str_int = str2int('12345')
print(str_int)
s = 'sdfaD'
s.upper()
lower = str.lower(s)


# filter()
# Python内建的filter()函数用于过滤序列。返回一个iterator
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1


f1 = filter(is_odd, [1, 2, 3, 4, 5, 6, 7])
print(list(f1))


# 把一个序列中的空字符串删掉
def not_empty(s):
    # 0，0L，0.0，0j，'',{},[],None 都是python定义的false
    y = 0 and 2
    # print(bool(y))
    return s and s.strip()


f_empty = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(f_empty)

# sorted
# Python内置的sorted()函数就可以对list进行排序：
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小倒序排序：
sort1 = sorted([1, -4, 5, -3, 12, -9])
sort2 = sorted([1, -4, 5, -3, 12, -9], key=abs, reverse=False)
print(sort1)
print(sort2)
# 默认情况下，对字符串排序，是按照ASCII的大小比较的
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 忽略大小写，按照字母序排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
itemgetter_test = itemgetter(0)
# 按名字排序
print(sorted(L, key=itemgetter_test))
# itemgetter_score,itemgetter_score2都是按照分数
itemgetter_score = itemgetter(1)
itemgetter_score2 = lambda t: t[1]
print(sorted(L, key=itemgetter_score2))
