import time
import math

def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        time_delata =  end - start
        # time_delata = round((end - start),10)
        print(func.__name__,f"花费时间大概{time_delata}毫秒")
        return time_delata
    return inner
@timer
def sayHello():
    print('hello')
sayHello()
