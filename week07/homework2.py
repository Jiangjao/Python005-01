def outer_arg(bar):
    def outer(func):
        def inner(*args,**kwargs):
            # 判断bar的类型
            if isinstance(bar,dict):
                print(' watch out a dict  ')
                try:
                    for index in range(len(bar)):
                        ret = func(bar[index])
                except Exception as error:
                    print(error)
                    
                # return 
            for index in range(len(bar)):
                ret = func(bar[index])
            print(bar)
            return ret
        return inner
    return outer

@outer_arg({'1':1,'2':2})
def sayHello(index=1):
    print(f'Hello Wolrd {index}')
    
# sayHello(1,2,3,4)
sayHello(1)