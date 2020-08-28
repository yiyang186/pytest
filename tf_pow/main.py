import tensorflow as tf

beta = 0.999

a = tf.Variable(0.)
global_step = tf.train.get_or_create_global_step()
global_step_f = tf.cast(global_step, tf.float32)
a = 1. - tf.pow(beta, global_step_f)
p1 = tf.print(':', a)

global_step = tf.assign_add(global_step, 1)
p2 = tf.print('global_step:', global_step)


with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  for i in range(100):
    sess.run([p1, p2])
    print('\n')


