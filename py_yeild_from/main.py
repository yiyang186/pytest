import time

def foo_c():
  for i in range(100):
    yield i, i+1


def foo_b(i):
  if i > 0:
    return 5, 6
  else:
    yield from foo_c()


class A:
  def __init__(self):
    self.s = 0
    self.flag = True 

  def __iter__(self):
    return self

  def __next__(self):
    if self.flag:
      self.gen = foo_b(-1)
      self.flag = False
      return next(self.gen)
    else:
      return next(self.gen)


class AA:
  def __init__(self):
    self.s = 0

  def __iter__(self):
    return self

  def __next__(self):
    time.sleep(0.2)
    self.s += 1
    return self.s

def runA():
  a = A()
  for i, j in a:
    print(i, j)

def runC():
  for xxx in foo_c():
    print(xxx)

def runB():
  print(foo_b(1))
  for xxx in foo_b(-1):
    print(xxx)

def runAA():
  aa = AA()
  for i, j in aa:
    print(i, j)

runA()
