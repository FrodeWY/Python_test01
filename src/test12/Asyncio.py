import asyncio as asyncio
import threading

import time
from datetime import datetime

import aiofiles as aiofiles


def read_file():
    print('start read (%s)' % threading.currentThread())
    with open('../resource/sina.html', 'r', encoding='utf-8') as f:
        content = f.readlines()
    with open('../resource/sina3.html', 'w', encoding='utf-8') as w:
        for val in content:
            w.write(val)
    print('end read(%s)' % threading.current_thread())


def thread_read_file():
    start = datetime.now().timestamp()
    t1 = threading.Thread(target=read_file, name='t1')
    t2 = threading.Thread(target=read_file, name='t1')
    t3 = threading.Thread(target=read_file, name='t1')
    t4 = threading.Thread(target=read_file, name='t1')
    t5 = threading.Thread(target=read_file, name='t1')
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    end = datetime.now().timestamp()
    print('thread time:', end - start)


async def async_read_file():
    print('start read (%s)' % threading.currentThread())
    # 使用Python 3.5或更高版本时，可以将aiofiles文件对象用作异步上下文管理器。异步迭代也被支持。
    # 当使用Python 3.3或3.4时，请注意关闭文件可能会阻塞，并且在从上下文管理器退出时从协程中产生是不可能的，因此aiofiles文件对象不能用作（普通的，非异步的）上下文管理器。使用try/finally介绍部分的结构来确保文件关闭。
    # 当使用Python 3.3或3.4时，迭代也不受支持。要迭代文件，请readline重复调用，直到返回空结果。请记住readline不去掉换行符。（https://github.com/Tinche/aiofiles/）
    async with aiofiles.open('../resource/sina.html', 'r', encoding='utf-8') as f:
        contents = await f.readlines()
    async with aiofiles.open('../resource/sina2.html', 'w', encoding='utf-8')as w:
        for val in contents:
            await w.write(val)
    print('async end read(%s)' % threading.current_thread())
    return contents


def async_read():
    start = datetime.now().timestamp()
    loop = asyncio.get_event_loop()
    task1 = loop.create_task(async_read_file())
    task2 = loop.create_task(async_read_file())
    task3 = loop.create_task(async_read_file())
    task4 = loop.create_task(async_read_file())
    task5 = loop.create_task(async_read_file())
    # tasks = asyncio.gather(task1,task2)
    tasks = [task1, task2, task3, task4, task5]
    loop.run_until_complete(asyncio.wait(tasks))
    # Future获取结果
    # for result in tasks._result:
    #     print(result)
    # task获取结果
    # for result in tasks:
    #     print(result.result())
    loop.close()
    end = datetime.now().timestamp()
    print('time:', end - start)


@asyncio.coroutine
def hello():
    print('Hello world (%s)' % threading.currentThread())
    r = yield from asyncio.sleep(1)
    print("Hello agein! %s" % threading.currentThread())
    return 'ss'


def hello_use1():
    loop = asyncio.get_event_loop()
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


def hello_use2():
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(hello())
    task1 = loop.create_task(hello())
    task2 = loop.create_task(hello())
    tasks = [task1, task2]
    results = loop.run_until_complete(asyncio.wait(tasks))
    for result in tasks:
        print(result.result())
    loop.close()


@asyncio.coroutine
def wget(host):
    print('wget %s ...' % host)
    connect = asyncio.open_connection(host, 80)
    read, write = yield from connect
    header = 'GET / HTTP/1.1\r\nHost: %s\r\n\r\n' % host
    write.write(header.encode('utf-8'))
    # 刷新写入的缓冲区
    yield from write.drain()
    while True:
        line = yield from read.readline()
        if line ==b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    write.close()


def start_wget():
    loop = asyncio.get_event_loop()
    task = [wget(host) for host in ['www.sina.com', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(task))
    loop.close()


if __name__ == '__main__':
    #     hello_use2()
    #     async_read()
    #     thread_read_file()
    start_wget()
