import tensorflow as tf

global_step = tf.train.get_or_create_global_step()
a = tf.random_uniform([], maxval=10, dtype=tf.int32)
b = a + 1

with tf.Session() as sess:
  init = tf.global_variables_initializer()
  sess.run(init)
  print(sess.run([global_step, a, b]))
  print(sess.run([global_step, b]))
  print(sess.run([global_step, a]))
  print(sess.run([global_step, b]))
