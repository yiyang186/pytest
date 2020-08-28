import tensorflow as tf

def _lighting(image, std, eigval=None, eigvec=None, scope=None):
  with tf.name_scope(scope, 'lighting', [image]):
    if eigval is None:
      eigval = tf.constant([0.2175, 0.0188, 0.0045], dtype=tf.float32) * 255.0

    if eigvec is None:
      eigvec = tf.constant(
          [[-0.5675, 0.7192, 0.4009],
           [-0.5808, -0.0045, -0.8140],
           [-0.5836, -0.6948, 0.4203]], dtype=tf.float32)

    alpha = tf.random_normal([3], stddev=std)
    eigval = alpha * eigval
    eigval = tf.reshape(eigval, [3, 1])
    noise = tf.matmul(eigvec, eigval)
    noise = tf.reshape(noise, [3])

    image = image + noise
  return image
