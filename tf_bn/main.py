import tensorflow as tf
slim = tf.contrib.slim

g = tf.Graph()
with g.as_default():
  is_training = tf.placeholder(tf.bool, [])
  input = tf.placeholder(tf.float32, [10, 10, 3])
  net = slim.batch_norm(input, is_training=is_training, scope='bn_1')
  net = slim.batch_norm(input, is_training=True, scope='bn_2')

  input1 = tf.placeholder(tf.float32, [10, 10, 3])
  net1 = slim.batch_norm(input1, is_training=False, scope='bn_3')

tf.summary.FileWriter('data', g)
