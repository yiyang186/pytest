from collections import deque

class T:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def __eq__(self, t):
    return self.a == t


dq = deque(maxlen=5)
dq.append(T('A', 0.5))
dq.append(T('B', 0.1))
dq.append(T('A', 0.2))
dq.append(T('C', 0.8))
dq.append(T('A', 0.9))

print(dq)
print(dq.count('A'))


