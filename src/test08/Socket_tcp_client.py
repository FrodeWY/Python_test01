import socket


def socket_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Addr = '192.168.16.111'
    # Addr = '127.0.0.1'
    s.connect((Addr, 9999))
    print(s.recv(1024).decode('utf-8'))
    # print((b''.join(buffer)).decode('utf-8'))
    for data in [b'Michael', b'Tracy', b'Sarch']:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()


if __name__ == '__main__':
    socket_client()
