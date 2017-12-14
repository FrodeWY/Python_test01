from multiprocessing.managers import BaseManager

import time
from queue import Queue

# QueueWorker.py处理任务，开多个可以实现分布式
class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# server_addr = '192.168.16.101'
server_addr = '127.0.0.1'
print('connect to server %s' % server_addr)

m = QueueManager(address=(server_addr, 6000), authkey=b'abc')
m.connect()
task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
    try:
        n = task.get(True)
        print('run task %d*%d...' % (n, n))
        r = '%d * %d =%d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except Exception as e:
        print('task queue is empty:', e)

print('worker exit.')
