# 1.content 为短信内容，超过 70 个字自动拆分成两条发送 
# 2.为 sendsms() 函数增加装饰器 send_times()，
# 通过装饰器方式实现限制手机号最多发送次数
# #!/usr/bin/env python
import redis
import time
import sys


client = fakeredis.FakeStrictRedis() # 测试 Redis

def send_times(times):
    def decorate(func):
        @wraps(func)
        def wrapper(telephone_number, content, times=5, key=None):
            con_len = len(content)
            if con_len < 70:
                dump(telephone_number,times)
            else:
                func(telephone_number, content[:con_len >> 2])
                func(telephone_number, content[con_len >> 2:])
            
        return wrapper
    return decorate

def dump(telephone_number, limit=5):
    """尝试发送短信"""
    # 短信发送逻辑, 作业中可以使用 print 来代替
    client.set(telephone_number,0,nx=True,ex=60)
    client.incr(telephone_number)
    if int(client.get(telephone_number))<= limit:
        print('发送成功')
    else:
        print(' 1 分钟内发送次数超过 5 次, 请等待 1 分钟')

if __name__ == '__main__':
   # 检查命令行参数个数
    if len(sys.argv) < 2:
        print('Please specify a phone number,it is a int type')
        exit(1)

    telephone_number = sys.argv[1]
    @send_times(times=5)
    def sendsms(telephone_number, content, key=None):
        client.rpush(telephone_number, time())
        