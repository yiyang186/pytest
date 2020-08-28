import tensorflow as tf
import numpy as np

w = np.arange(36, dtype=np.float32).reshape(3,3,2,2)
w = w * np.array([.0, .1], dtype=np.float32)# .reshape((-1, 1))
wt = tf.convert_to_tensor(w)

input = np.ones((1, 2, 2, 2), dtype=np.float32)
it = tf.convert_to_tensor(input)

output_shape = [1, 4, 4, 2]
out = tf.nn.conv2d_transpose(it, wt, output_shape=output_shape,
    strides=[1,2,2,1], padding='SAME')
# out = out * np.array([.0, .1], dtype=np.float32)

with tf.Session() as sess:
  print(sess.run(out))

