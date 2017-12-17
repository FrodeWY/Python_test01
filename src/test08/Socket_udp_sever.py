import socket
import threading

import time

# UDP的使用与TCP类似，但是不需要建立连接。此外，
# 服务器绑定UDP端口和TCP端口互不冲突，也就是说，
# UDP的9999端口与TCP的9999端口可以各自绑定。
def udp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('0.0.0.0', 9999))
    print('Bind UDP on 9999..')
    while True:
        # recvfrom()方法返回数据和客户端的地址与端口
        data, addr = s.recvfrom(1024)
        time.sleep(1)
        t = threading.Thread(target=tplink, args=(s, data, addr))
        t.start()


def tplink(socket, data, addr):
    print('connect form %s :%s' % addr)
    # 调用sendto()就可以把数据用UDP发给客户端。
    socket.sendto(b"hello,%s" % data, addr)
    print('connect %s:%s close..' % addr)



if __name__ == '__main__':
    udp_server()