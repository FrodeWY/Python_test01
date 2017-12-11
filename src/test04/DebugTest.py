# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError：

import sys

import logging


# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
# logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。
# 同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
def foo(s):
    n = int(s)
    # assert n != 0, 'n is zero'
    logging.basicConfig(level=logging.INFO)  # 设置输出日志等级默认warning
    logging.info('n=%d' % n)  # logging.info()就可以输出一段文本
    logging.warning('n=%d' % n)  # logging.info()就可以输出一段文本
    logging.debug('n=%d' % n)  # logging.info()就可以输出一段文本
    r = 10 / n
    return r


def main():
    foo('0')


main()
print(sys.path)
