import tensorflow as tf
from tensorflow.core.framework import summary_pb2


g = tf.Graph() 
writer = tf.summary.FileWriter('event1', g)
for i in range(100):
  summ = summary_pb2.Summary()
  value = summ.value.add()
  value.tag = 'c'
  value.simple_value = float(i)
  writer.add_summary(summ, i)
