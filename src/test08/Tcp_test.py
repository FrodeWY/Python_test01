import socket


# 创建Socket时，AF_INET指定使用IPv4协议，
# 如果要用更先进的IPv6，就指定为AF_INET6。
# SOCK_STREAM指定使用面向流的TCP协议。
# 80端口是Web服务的标准端口
# 端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用
def socket01():
    # 创建一个基于TCP连接的Socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('www.sina.com.cn', 80))
        s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
        buffer = []
        while True:
            d = s.recv(1024)
            if d:
                buffer.append(d)
            else:
                break
        data = b''.join(buffer)
        print(data.decode('utf-8'))
        # 连续两个\r\n时，Header部分结束，后面的数据全部是Body
        header,html=data.split(b'\r\n\r\n',1)
        print(header.decode('utf-8'))
        with open('../resource/sina.html','wb') as f:
            f.write(html)
    finally:
        s.close()

if __name__ == '__main__':
    socket01()
