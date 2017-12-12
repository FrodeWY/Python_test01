import threading

import time

lock = threading.Lock()  # 创建一个锁


def loop():
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s ended." % threading.current_thread().name)


balance = 0


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


# 多线程和多进程最大的不同在于，多进程中，同一个变量，
# 各自有一份拷贝存在于每个进程中，互不影响，而多线程中，
# 所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
# 因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
def run_thread(n):
    for i in range(1000000):
        change_it(n)


def run_thread_lock(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


def start_loop():
    print("thread %s is running..." % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print("thread %s is ended" % threading.current_thread().name)


def start_change():
    t1 = threading.Thread(target=run_thread, args=(5,), name='t1')
    t2 = threading.Thread(target=run_thread, args=(18,), name='t2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)


def start_change_lock():
    t1 = threading.Thread(target=run_thread_lock, args=(5,), name='t1')
    t2 = threading.Thread(target=run_thread_lock, args=(18,), name='t2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)


if __name__ == '__main__':
    # start_loop()
    # start_change()  # 没有上锁，有可能会导致全局变量结果异常

    start_change_lock()
