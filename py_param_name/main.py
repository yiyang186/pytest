class A:
  def foo(self, a, b):
    pass

  def xxx(self, a, b):
    return self.foo(a, b)


class B(A):
  def foo(self, c, d):
    return c + d


b = B()
r = b.xxx(1, 2)
print(r)
