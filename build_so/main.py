from future import print_function

from a.aa import foo
from b.bb import fooc
from b import dd

foo(1, 2, 3)
fooc(4)
dd.food(5)
dd.fooe(6, a=1, b=2)

