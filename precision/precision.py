from decimal import *


class Element:

  def  __init__(self, value):
    self.exact = Decimal(value)
    self.value = value
    self.loss = Decimal(0)

  def float32(self):
    origin = self.exact
    self.value = float(self.value)
    self.exact = Decimal(self.value)
    self.loss = self.exact - origin
    return self

  def int32(self):
    origin = self.exact
    self.value = int(self.value)
    self.exact = Decimal(self.value)
    self.loss = self.exact - origin
    return self

  def __add__(self, value):
    self.exact = self.exact + Decimal(value)
    self.value = self.value + value

    origin = self.exact
    self.exact = Decimal(self.value)
    self.loss = self.exact - origin
    return self

  def __sub__(self, value):
    self.exact = self.exact - Decimal(value)
    self.value = self.value - value

    origin = self.exact
    self.exact = Decimal(self.value)
    self.loss = self.exact - origin
    return self

  def __mul__(self, value):
    self.exact = self.exact * Decimal(value)
    self.value = self.value * value

    origin = self.exact
    self.exact = Decimal(self.value)
    self.loss = self.exact - origin
    return self

  def __div__(self, value):
    self.exact = self.exact / Decimal(value)
    self.value = self.value / value

    origin = self.exact
    self.exact = Decimal(self.value)
    self.loss = self.exact - origin
    return self


class NumberBase:

  def __init__(self, value):
    self.origin = Element(value)
    self.current = Element(value)
    self.losses = list()

  def float32(self):
    self.current.float32()
    self.losses.append(('float32', self.current.loss))
    return self

  def int32(self):
    self.current.int32()
    self.losses.append(('int32', self.current.loss))
    return self

  def __add__(self, value):
    self.current = self.current + value
    self.losses.append(('add', self.current.loss))
    return self

  def __sub__(self, value):
    self.current = self.current - value
    self.losses.append(('add', self.current.loss))
    return self

  def __mul__(self, value):
    self.current = self.current * value
    self.losses.append(('mul', self.current.loss))
    return self

  def __div__(self, value):
    self.current = self.current / value
    self.losses.append(('div', self.current.loss))
    return self

  def loss(self):
    return sum(x[1] for x in self.losses)
