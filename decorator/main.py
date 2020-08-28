def decorator(func):
  def wrapper(x):
    print('wrap ...')
    yield from func(x)
  return wrapper

# @decorator
# def foo(x):
# equal to
# foo == decorator(foo)
@decorator
def generator(x):
  for i in range(x):
    yield i

print(type(generator))

for i in generator(10):
  print(i)
