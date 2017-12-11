# 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
import logging

# logging.basicConfig函数各参数:
# filename: 指定日志文件名
# filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
# format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
# %(levelno)s: 打印日志级别的数值
# %(levelname)s: 打印日志级别名称
# %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
# %(filename)s: 打印当前执行程序名
# %(funcName)s: 打印日志的当前函数
# %(lineno)d: 打印日志的当前行号
# %(asctime)s: 打印日志的时间
# %(thread)d: 打印线程ID
# %(threadName)s: 打印线程名称
# %(process)d: 打印进程ID
# %(message)s: 打印日志信息
# datefmt: 指定时间格式，同time.strftime()
# level: 设置日志级别，默认为logging.WARNING
# stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略
import sys

# logging.basicConfig(level=logging.ERROR, filename='../resource/exception.log')  # 日志等级为error的写入日志文件中


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————
log = logging.getLogger()  # 获取logging 对象
handler = logging.FileHandler('../resource/exception.log')  # 设置日志文件处理器
handler.setLevel(logging.WARNING)  # 设置日志文件等级
log.addHandler(handler)  # 将日志文件处理器加入loggin实例
log.setLevel(logging.DEBUG)  # 设置控制台日志等级
console = logging.StreamHandler()  # 获取streamHandler
log.addHandler(console)  # 将streamHandler添加到logging实例，从而使控制台输出日志


def try_catch(a):
    try:
        print("try:")
        r = 10 / int(a)
        print("excute")
    except ZeroDivisionError as e:
        print('except:', e)
    except ValueError as e:
        print("except:", e)
    else:
        print('no error')
    finally:
        print('end')
    print("test end!")


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print(11)
        logging.exception(e)


main()
log.debug("debug test")
log.info("info test")
log.warning('warning test')

# logging.debug("debug test")
# logging.info("info test")
# logging.warning('warning test')
if __name__ == '__main__':
    print(1221)
    try_catch('5')

print('end test')


class FooError(ValueError):
    pass


# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。
# Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
def foo2(s):
    n = int(s)
    if n == 0:
        logging.exception(FooError)
        raise FooError("FooError")
    return 10 / n


print(foo2(0))


# 捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
def bar2(s):
    try:
        n = 10 / s
    except ZeroDivisionError as e:
        print('zero error')
        raise
        # raise ValueError('value error')
    print('bar2 end')


bar2(0)
