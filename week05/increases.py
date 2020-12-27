# !/usr/bin/python

# 使用Python + Redis实现高并发的计数器
# counter 利用redis实现自增操作实现的函数，每调用一次，计数+1
# param:video_id,唯一
import redis

def counter(client,video_id: int):
    
    client.incr(f'{video_id}',amount=1)
    count_number = client.get(f"{video_id}")
    # print(count_number)
    return count_number.decode()

def main():
    # 连接Redis
    client = client = redis.Redis(host='localhost',password='dasdf')

    counter(client,10010)
    # print(client.keys())

if __name__ =='__main__':
    main()






