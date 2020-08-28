import tensorflow as tf


def build_graph(a_, b_):
  g = tf.Graph()
  with g.as_default():
    a = tf.constant(a_)
    b = tf.constant(b_)
    c = a + b

  conf = tf.ConfigProto(allow_soft_placement=True,
                        log_device_placement=True)
  sess = tf.Session(graph=g, config=conf)
  return sess, c

with tf.device('/gpu:0'):
  sess1, output1 = build_graph(1, 2)

with tf.device('/cpu:0'):
  sess2, output2 = build_graph(3, 4)

print(sess1.run(output1))
print(sess2.run(output2))
