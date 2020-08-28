class A:
  def __init__(self):
    self.__build()

  def __build(self):
    print('A')


class B(A):
  def __init__(self):

    self.__build()

  def __build(self):
    print('B')


b = B()
