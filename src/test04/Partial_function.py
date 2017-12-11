# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
import functools

import sys

print(int("12345", base=8))  # 将8进制转为10进制


def int8(x, base=2):  # 将2进制转为10进制
    return int(x, base)


i8 = int8("10")
print(i8)
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
partial_int2 = functools.partial(int, base=2)
print(partial_int2("10"))
# 注意到上面的新的partial_int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：
print(partial_int2('10', base=10))
print(partial_int2('10'))


def test():
    args = sys.argv
    if len(args) == 1:
        print('args 1')
    elif len(args) > 1:
        print('args>1')


# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
# 最常见的就是运行测试。
if __name__ == '__main__':
    test()
