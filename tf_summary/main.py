import tensorflow as tf
from tensorflow.core.framework import summary_pb2

def parse_summay(s):
  summ = summary_pb2.Summary()
  summ.ParseFromString(s)
  return summ


g = tf.Graph() 
with g.as_default():
  a = tf.placeholder(tf.float32, [], name='a')
  b = tf.placeholder(tf.float32, [], name='b')
  c = a + b
  sop = tf.summary.scalar('c', c)

writer = tf.summary.FileWriter('.', g)
sess = tf.Session(graph=g)

with sess.as_default():
  for i in range(100):
    s = sess.run(sop, feed_dict={a: i, b: i + 1})
    writer.add_summary(s, i)
    summ = parse_summay(s)
    import pdb; pdb.set_trace()
