import socket
import threading

import time


def socket_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定监听的地址和端口,端口号需要预先指定。因为我们写的这个服务不是标准服务，所以用9999这个端口号。请注意，小于1024的端口号必须要有管理员权限才能绑定：
    s.bind(('0.0.0.0', 9999))
    # $ 调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
    s.listen(5)
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


def tcplink(sock, addr):
    print('Accept new connection from %s:%s' % addr)
    sock.send(b'welcome!')
    # print(sock.recv(1024).decode('utf-8'))
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


if __name__ == '__main__':
    socket_server()
