import os
import random

import time
from multiprocessing.pool import Pool


# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
def long_time_task(name):
    print('run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
    return name


# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。

# 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，
#  因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制
# apply_async 非阻塞
def pool01():
    print("Parent process %s." % os.getpid())
    p = Pool(7)
    result = []
    for i in range(10):
        result.append(p.apply_async(long_time_task, args=(i,)))
    print('waiting for all subProcesses done...')
    p.close()
    p.join()
    print('All subProcesses done')
    for name in result:
        print(type(name))  # 非阻塞的返回的结果为ApplyResult
        print(name.get())


# apply 阻塞
def pool02():
    print("Parent process %s." % os.getpid())
    p = Pool(7)
    result = []
    for i in range(10):
        result.append(p.apply(long_time_task, args=(i,)))
    print('waiting for all subProcesses done...')
    p.close()
    p.join()
    print('All subProcesses done')
    for name in result:
        print(name)  # 阻塞的直接返回最终的结果


if __name__ == '__main__':
    pool01()
