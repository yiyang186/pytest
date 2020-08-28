import tensorflow as tf
from tensorflow.contrib import slim
from tensorflow.contrib import quantize

def arg_scope():
    with slim.arg_scope(
      [slim.conv2d, slim.fully_connected, slim.conv2d_transpose],
      activation_fn=tf.nn.relu,
      normalizer_fn=slim.batch_norm),\
         slim.arg_scope(
      [slim.conv2d, slim.max_pool2d, slim.conv2d_transpose],
      padding='SAME',
      data_format='NHWC') as sc:
      return sc

def net():
  img = tf.placeholder(tf.float32, [None, 256, 256, 3])
  conv1 = slim.conv2d(img, 64, [3, 3], scope='conv1')
  pool1 = slim.avg_pool2d(conv1, [2, 2], scope='pool1')

  conv2 = slim.conv2d(img, 64, [3, 3], stride=2, scope='conv2')
  sc1 = tf.add(conv2, pool1, name='sc1')

  conv3 = slim.conv2d(sc1, 128, [3, 3], stride=2, scope='conv3')
  downsample1 = tf.image.resize_nearest_neighbor(sc1, [64, 64],
      name='nearest_neighbor_downsample')
  concat1 = tf.concat([conv3, downsample1], axis=3, name='concat1')

  dconv1 = slim.conv2d_transpose(concat1, 128, [3, 3],
      stride=2, scope='dconv1')
  upsample1 = tf.image.resize_images(concat1, [128, 128])

  concat2 = tf.concat([dconv1, upsample1], axis=3, name='concat2')

  conv4 = slim.conv2d(upsample1, 128, [1, 1], scope='conv4')
  conv5 = slim.conv2d(concat2, 128, [1, 1], scope='conv5')
  sc2 = tf.add(conv4, conv5, name='sc2')

  pool2 = tf.reduce_mean(sc2, axis=[1,2], name='global_average_pool')
  return pool2



g = tf.Graph()
with g.as_default():
  with slim.arg_scope(arg_scope()):
    end = net()
    quantize.create_training_graph(input_graph=g,
      quant_delay=2000000)

tf.summary.FileWriter('.', g)
