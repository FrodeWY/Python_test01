import asyncio
from aiohttp import web
import aiomysql

@asyncio.coroutine
def test_example(loop):
    cn = yield from aiomysql.connect(host='localhost',
                                     user='root',
                                     password='123456',
                                     db='wangyang01',
                                     loop=loop)

    cur = yield from cn.cursor()
    yield from cur.execute("select *  from EMPLOYEE")
    r = yield from cur.fetchone()
    result = r[0]
    yield from cur.close()
    cn.close()
    return str(result)

@asyncio.coroutine
def hello(request):
    r = yield from test_example(request.app.loop)
    return web.Response(body=b"hello world" + r.encode())

app = web.Application()
app.router.add_route('GET', '/', hello)

if __name__ == '__main__':
    web.run_app(app, port=9000)