import queue
import random

from multiprocessing.managers import BaseManager

from multiprocessing import freeze_support
# ManagersMaster.py分配任务
task_queue = queue.Queue()
result_queue = queue.Queue()


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


class QueueManager(BaseManager):
    pass


def queue_master():
#   windows中callable不支持lambda（callable=lambda:task_queue）
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
# address=('', 6000)unix，linux系统中，给''才能连接正常，windows必须给127.0.0.1或localhost
    manager = QueueManager(address=('127.0.0.1', 6000), authkey=b'abc')
    manager.start()
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    for i in range(10):
        n = random.randint(0, 1000)
        print('put task %d....' % n)
        task.put(n)

    print('Try get results')
    for i in range(10):
        r = result.get(True)
        print("result :%s" % r)

    manager.shutdown()
    print("master exit.")


if __name__ == '__main__':
    # freeze_support()
    #windows 中multiprocessing下的进程必须在main方法中运行
    queue_master()
