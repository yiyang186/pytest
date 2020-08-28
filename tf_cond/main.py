import tensorflow as tf

a = tf.Variable(10., name='a')
b = tf.Variable(20., name='b')

c = a + b
d = b - a

def change(a, b):
  aa = tf.assign_add(a, 1.)
  ab = tf.assign_add(b, 1.)
  return [aa, ab]

e = tf.Variable(True)
f = tf.cond(e, lambda :change(a, b),
               lambda: [d, b])

with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  f_ = sess.run(f)
  print(f_)
  a_, b_ = sess.run([a, b])
  print(a_, b_)
  
