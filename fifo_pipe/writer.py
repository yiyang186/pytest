import pickle
import numpy as np
import os

a = {'a': np.arange(0, 1000000, 1)}
aa = pickle.dumps(a)
FIFO = 'mypipe'

# os.mkfifo(FIFO)

with open(FIFO, 'wb') as fifo:
  fifo.write(aa)
