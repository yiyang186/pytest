import os
import errno
import pickle

FIFO = 'mypipe'

try:
  os.mkfifo(FIFO)
except OSError as oe: 
  if oe.errno != errno.EEXIST:
    raise

print("Opening FIFO...")
while True:
  with open(FIFO, 'rb') as fifo:
    ret = fifo.read()
    ret = pickle.loads(ret)
    print(ret['a'].size)
