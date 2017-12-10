def sum_lazy(*t):
    def sum():
        ax = 0
        for i in t:
            ax += i
        return ax

    return sum


#  当我们调用sum_lazy()时，返回的并不是求和结果，而是求和函数,调用函数lazy时，才真正计算求和的结果：
# 我们在函数sum_lazy中又定义了函数sum，并且，内部函数sum可以引用外部函数lsum_lazy的参数和局部变量，
# 当sum_lazy返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力
lazy = sum_lazy(1, 2, 3)
print(type(lazy))
print(lazy())
lazy2 = sum_lazy(1, 2, 3)
print(lazy == lazy2)
a, b, c = [1, 3, 4]
print(a, b, c)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
f1, f2, f3 = count()
print(f1(), f2(), f3())

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
import src.test04.Partial_function


def count2():
    fs = []

    def f1(j):
        def f():
            return j * j

        return f

    for i in range(1, 4):
        fs.append(f1(i))
    return fs


f4, f5, f6 = count2()
print(f4(), f5(), f6())
