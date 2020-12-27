# #!/usr/bin/env python
# 每分钟最多发送五次，请基于Python和Redis实现接口

import redis
import time


def count_time(client,phone_number: int):
    send_time = time.time()
    print(int(round(send_time*1000 )))

    client.rpush(f'{phone_number}:id',int(round(send_time*1000 )))
    if client.llen(f'{phone_number}:id') > 4:
        pre = client.lindex(f'{phone_number}:id', 0).decode()
        nex = client.lindex(f'{phone_number}:id', 3).decode()
        if int(nex) - int(pre) > 6000:
            print('more than 5 times, 请等待 1 分钟')
            return 
    

def sendsms(client,phone_number: int,contents:str,key:None):

    # 先判断一分钟内
    count_time(phone_number)

    client.incr(f'{phone_number}',amount=1)
    count_number = client.get(f"{phone_number}")
    send_times_count = int(count_number.decode())
    # client.hset(f'phone_number',count_number,'v1')
    
    print('=====')
    
    if  send_times_count > 4:
        
        print('1 分钟内发送次数超过 5 次, 请等待 1 分钟')
        # 在判断五次
    else:
        print('发送成功',phone_number,contents)
    # print(count_number)
    # return count_number

sendsms(10121)
def main(telephone_number:int):
    # 连接Redis
    client = redis.Redis(host='localhost',password='Dj970903')

    try:
        while True:
            sendsms()
    except KeyboardInterrupt:
        print('have a look')

    print(client.keys())

    for key in client.keys():
        print(key.decode())
    count_number = 0