#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

def timing_function(any_function):
    """
    out put the time a function takes to execute.
    """
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = any_function(*args, **kwargs)
        t2 = time.time()
        print( "Time it took to run the functions: {:0.20f}".format( (t2-t1)) )
        return result

    return wrapper

@timing_function
def my_function():
    num_list = []
    for num in xrange(0, 10000):
        num_list.append(num)
    print("\nSum of all the numbers: " + str(sum(num_list)))


if __name__ == '__main__':
    #print(my_function())
    my_function()
