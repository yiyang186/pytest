import tensorflow as tf

g = tf.Graph()
with g.as_default():
  a = tf.constant(9)
  b = tf.constant(0)
  c = tf.constant(False)
  
  d = tf.cond(c, lambda: a, lambda: b)

with tf.Session(graph=g) as sess:
  print(sess.run(d))


def fa(xx):
  a = tf.constant(9) + xx
  # tf.summary.scalar('a', a)
  return a

def fb(xx):
  b = tf.constant(0) + xx
  tf.summary.scalar('b', b)
  return b

g1 = tf.Graph()
with g1.as_default():
  c = tf.constant(False)
  x = tf.constant(1)

  # d = tf.cond(c, lambda: fa(x),
  #                lambda: fb(x))
  a = fa(x)
  b = fb(x)
  d = tf.where(c, a, b)
  
  summary_op = tf.get_collection(tf.GraphKeys.SUMMARIES)
  print(summary_op)

with tf.Session(graph=g1) as sess:
  print(sess.run(d))
  sess.run(summary_op)
