import os

# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
# 因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
# 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，
# 父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
# Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：
# Windows没有fork调用，上面的代码在Windows上无法运行
from multiprocessing import Process


def fork01():
    print("Process (%s) start..." % os.getpid())
    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# multiprocessing模块就是跨平台版本的多进程模块。
# multiprocessing模块提供了一个Process类来代表一个进程对象
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    # fork01()
    print("parent process %s" % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('child process will start .')
    p.start()
    p.join()
    print('child process end.')
