def sayHello(index=1):
    print(f'Hello Wolrd {index}')

def my_map(fun,*iterations):
    m = len(iterables)
    try:
        n = len(iterables[0])
    except TypeError as e:
        raise TypeError('please input iterables')
    for items in zip(*iterations):
	    yield fun(*items)

# sayHello(1,2,3,4)

my_map(sayHello,{'1':1,'2':2})