from multiprocessing import Process, Manager

class A:
  def __init__(self):
    self.manager = Manager()

  def run(self, st):
    procs = []
    rd = self.manager.dict()
    for i in range(5):
      p = Process(target=self.foo, args=(i, st, rd))
      p.start()
      procs.append(p)

    for i in range(5):
      procs[i].join()

    print(rd.values())

  def foo(self, i, st, rd):
    rd[i] = st + i + 1

a = A()
a.run(0)
a.run(10)

