import asyncio as asyncio
import threading

import time


@asyncio.coroutine
def read_file():
    with open('../resource/1.jpg', 'rb') as f:
        time.sleep(1)
        return f.readlines()


@asyncio.coroutine
def hello():
    print('Hello world (%s)' % threading.currentThread())
    f = open('../resource/1.jpg', 'rb')
    # print(f.readline())
    r = yield from asyncio.sleep(1)
    f.close()
    print("Hello agein! %s" % threading.currentThread())
    return 'ss'


def hello_use():
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(hello())
    tasks = [hello(), hello()]
    results = loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


@asyncio.coroutine
def wget(host):
    print('wget %s ...' % host)
    connect = asyncio.open_connection()

if __name__ == '__main__':
    hello_use()