# #!/usr/bin/env python
# 每分钟最多发送五次，请基于Python和Redis实现接口

import redis
import time
import sys

def count_time(bracket:list, limit: int):
    # 不超过limit次数
    if len(bracket) < limit:
        return True
    
    # 获取倒数第limit次的发送时间
    latest_time = float(list[:-limit].decode())
    now = time.time()

    # 事件差小于60seconds
    if now - latest_time < 60:
        return False
    else:
        return True
    

def sendsms(client,phone_number: int,contents:str,key:None):

    limit = 5
    bracket = client.lrange(phone_number,0,-1)
    if count_time(bracket, limit):
        # 本次发送时间添加到列表末尾
        client.rpush(phone_number, time.time())
        # 发送时间列表表头出队，减少存储空间
        if len(bracket) >= limit -1:
            client.ltrim(phone_number, -limit, -1)
        print('发送成功', phone_number, contents)
    else:
        print(phone_number,'1 分钟内发送次数超过 5 次, 请等待 1 分钟')



def main(phone_number:int):
    # 连接Redis
    client = redis.Redis(host='localhost',password='password')

    try:
        while True:
            sendsms(client, phone_number,'nihao')
            time.sleep(1)
    except KeyboardInterrupt:
        print('have a look')

if __name__ == '__main__':
   # 检查命令行参数个数
    if len(sys.argv) < 2:
        print('Please specify a phone number,it is a int type')
        exit(1)

    telephone_number = sys.argv[1]
    main(telephone_number)
