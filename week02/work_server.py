# !/usr/bin/python
import socket

HOST = "localhost"
PORT = 10000

def echo_server():
    """
    Echo Server 的 Server 端
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 对象s绑定到指定的主机和端口上
    s.bind((HOST,PORT))
    # 只接受1个连接
    s.listen(1)
    while True:
        # accept表示接受客户端的连接
        conn, addr = s.accept()
        # 输出客户端地址
        print(f'Connected by {addr}')
        file = open('results.log','a+')
        try:
            while True:
                try:
                    data = conn.recv(1024)
                except ConnectionAbortedError as e:
                    print('connect disrupted or finished task!')
                    exit(0)
                if not data:
                    print('no data')
                    exit(0)
                    break
                elif data.decode('utf-8') == 'quit.EOF':
                    exit(1)
                else:
                    conn.send(b'file send successful!')
                    file.write(data.decode('utf-8'))
                    print('file accept successful!')
        except Exception as e:
            print(f'File acceptance error -> {e}')
            s.send(b'File acceptance failed!')
        finally:
            file.close()
        conn.close()
    s.close()


if __name__ == "__main__":
    echo_server()