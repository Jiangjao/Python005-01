# !/usr/bin/env python
import socket

HOST = 'localhost'
PORT = 10000

def echo_client():

    '''Echo Server 的Client 客户端'''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    
    with open("transforfile.txt","r+") as f:
        for line in f.readlines():
            s.send(line.encode('utf-8'))
    print('send all up to')
    s.close()

if __name__ == '__main__':
    echo_client()




