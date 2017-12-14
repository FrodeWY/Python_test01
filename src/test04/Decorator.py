import functools


def now():
    print("2017/05/06")


# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
n = now
n()
# 函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__)
print(n.__name__)


def log(text='excute'):
    def decorator(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            print('%s  %s' % (text, fun.__name__))
            return fun(*args, **kwargs)

        return wrapper

    return decorator


# 函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的
@log("excute")
def now2(a, b):
    print("2017/05/06")
    print(a + b)


now2(1, 2)
print(now2.__name__)
