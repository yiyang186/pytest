import tensorflow as tf

def my_initializer(v):
  return v.initialized_value() + 2

v = tf.get_variable("v", shape=(), initializer=tf.zeros_initializer(),
    trainable=False)
w = tf.get_variable("w", initializer=v.initialized_value() + 1)
u = tf.get_variable("u", initializer=my_initializer(v))

global_variables = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES)
print('global_variables',
    *[v.name for v in global_variables], sep='\n')
trainable_variables = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES)
print('trainable_variables',
    *[v.name for v in trainable_variables], sep='\n')

with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  print(u.eval(), w.eval(), v.eval())
