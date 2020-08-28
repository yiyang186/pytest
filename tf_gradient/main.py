import tensorflow as tf

g1 = tf.Graph()
with g1.as_default():
  wa = tf.Variable([[1, 2]], dtype=tf.float32, trainable=True)

  with tf.variable_scope('round'):
    wa_round = tf.round(wa)
    wa_stop = tf.stop_gradient(wa_round - wa)
    wa_new = wa + wa_stop

  wb = tf.Variable([[3, 4]])

  wc = tf.Variable([[2], [1]], dtype=tf.float32, trainable=True)
  
  res = tf.matmul(wa_new, wc)
  
  grads = tf.gradients(res, [wa])

with tf.Session(graph=g1) as sess:
  tf.global_variables_initializer().run()
  re = sess.run(grads)
  print(re)


g2 = tf.Graph()
with g2.as_default():
  w1 = tf.get_variable('w1', shape=[3])
  w2 = tf.get_variable('w2', shape=[3])
  
  w3 = tf.get_variable('w3', shape=[3])
  w4 = tf.get_variable('w4', shape=[3])
  
  z1 = w1 + w2+ w3
  z2 = w3 + w4
  
  grads = tf.gradients(
    [z1, z2], [w1, w2, w3, w4],
    grad_ys=[tf.convert_to_tensor([2.,2.,3.]),
             tf.convert_to_tensor([3.,2.,4.])]
    )

with tf.Session(graph=g2) as sess:
  tf.global_variables_initializer().run()
  print(sess.run(grads))


g3 = tf.Graph()
with g3.as_default():
  input = tf.constant([-0.1, 0., 0.1, 0.11, 0.2, 10.1], dtype=tf.float32)
  s = tf.Variable([0.01], dtype=tf.float32, name='scale')
  z = tf.Variable([127], dtype=tf.float32, name='zero')

  with tf.variable_scope('scale_round'):
    q = tf.divide(input, s)
    q_round = tf.round(q)
    q_stop = tf.stop_gradient(q_round - q)
    q = q + q_stop

  with tf.variable_scope('zero_round'):
    z_round = tf.round(z)
    z_stop = tf.stop_gradient(z_round - z)
    z_int = z + z_stop

  q = q + z_int
  q = tf.clip_by_value(q, 0., 255., name='Saturate')

  with tf.variable_scope('de_quant'):
    r = s * (q - z_int)

  grads = tf.gradients(r, [q, s, z, z_int, input])
  # gq, gs, gz, gz_int, g_input = grads
  # gq = tf.identity(gq, name='grad_q')
  # gs = tf.identity(gs, name='grad_s')
  # gz = tf.identity(gz, name='grad_z')
  # gz_int = tf.identity(gz_int, name='grad_z_int')
  # g_input = tf.identity(g_input, name='grad_input')

  with tf.variable_scope('mse'):
    loss = tf.reduce_mean(tf.square(input - r))

  sgd = tf.train.GradientDescentOptimizer(0.01)
  grads_vars = sgd.compute_gradients(loss, var_list=[s, z])
  update_vars = sgd.apply_gradients(grads_vars)


writer = tf.summary.FileWriter('./g3', g3)
writer = tf.summary.FileWriter('./g2', g2)

with tf.Session(graph=g3) as sess:
  tf.global_variables_initializer().run()
  print('q s z z_int input'.split())
  print(*sess.run(grads), sep='\n')
  print(*sess.run([input, q, r]), sep='\n')
  print('grads_vars')
  print(*sess.run([grads_vars]), sep='\n')

