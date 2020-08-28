class Singleton(type):
  def __init__(self, *args, **kwargs):
    self.__instance = None
    super().__init__(*args, **kwargs)

  def __call__(self, *args, **kwargs):
    if self.__instance is None:
      self.__instance = super(Singleton, self).__call__(*args, **kwargs)
      return self.__instance
    else:
      return self.__instance

class A(metaclass=Singleton):
  def __init__(self, xx):
    self.xx = xx

  def __str__(self):
    return str(self.xx)
