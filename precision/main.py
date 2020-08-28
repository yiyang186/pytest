from precision import *

a = NumberBase(1)
b = a.float32() + 100
c = b * 10.2
print(c.losses)
print(c.loss())
