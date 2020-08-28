import numpy as np

def hello(s):
    print("hello world")
    print(s)
    print(np.arange(9).reshape(3,3))
 
 
def arg(a, b):
    print('a=', a)
    print('b=', b)
    return a + b
 
 
class Test:
    def __init__(self):
        print("init")
 
    def say_hello(self, name):
        print("hello", name)
        return name
