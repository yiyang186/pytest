import tensorflow as tf


g = tf.Graph()
with g.as_default():
  # a = tf.get_variable('a', shape=[])
  a = tf.Variable([100.6], dtype=tf.float32)
  b = 5 * a
  ra = tf.round(a)
  fa = tf.floor(a)
  gb = tf.gradients([b], [a])
  grads = tf.gradients([fa, ra], [a])
  cast_a = tf.cast(a, tf.int32)
  int_b = cast_a + tf.constant(1)
  grads_cast_b = tf.gradients([int_b], [cast_a])
  grads_cast_a = tf.gradients([cast_a], [a])

  c = tf.cast(a, tf.float64)
  grads_cast_c = tf.gradients([c], [a])

with tf.Session(graph=g) as sess:
  tf.global_variables_initializer().run()
  print(sess.run([a, b, ra, fa, cast_a]))
  print(sess.run(gb))
  # g = sess.run(grads)  #  <== raise Error
  # print(g)
  # g_cast_b = sess.run(grads_cast_b)  #  <== raise Error
  # print(g_cast_b)
  # g_cast_a = sess.run(grads_cast_a)  #  <== raise Error
  # print(g_cast_a)
  g_cast_c = sess.run(grads_cast_c)
  print(g_cast_c)

print(tf.__version__)
