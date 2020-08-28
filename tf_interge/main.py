import tensorflow as tf

a = tf.constant([1.])

with tf.Session() as sess:
  xa = sess.run(a)
  print(type(xa))
  print(xa)
