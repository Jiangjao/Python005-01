import logging
import time
from functools import wraps
"""
    record the time of function to file
"""

def logit(logfile="/var/log/python/test.log"):
    """
    param:logfile has to assigned 
    
    This is logging
    """
    def logging_decorator(a_func):
        @wraps(a_func)
        def with_logging():
            # print("info message:The funtion of %s has been called " % a_func.__name__)
            ss = time.strftime("%y-%m-%d-%H:%M:%S",time.localtime())
            logfile = "/var/log/python/%s/test.log" % ss
            logging.basicConfig(filename=logfile,
                                level=logging.DEBUG,
                                datefmt=ss,
                                format='%(asctime)s %(name)-8s %(levelname)-8s [line:%(lineno)d] %(message)s')
            logging.info("info message:The funtion of %s has been called " % a_func.__name__)  

        return with_logging
    return logging_decorator

if __name__ == "__main__" :
    print("Finised!")
    @logit()
    def test():
        print('hello')
    test()


