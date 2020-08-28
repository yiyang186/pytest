import tensorflow as tf
import numpy as np

stride = 1
kernel_size = 3
input_size = 35

output_size = (input_size + stride - 1) // stride
padding_needed = max(0, (output_size - 1) * stride + kernel_size - input_size)
padding_before = padding_needed // 2 
padding_after = padding_needed - padding_before

print(padding_before, padding_after)

a = np.arange(input_size ** 2).reshape((1,input_size,input_size,1))
ta = tf.convert_to_tensor(a)
out_max = tf.nn.pool(ta, [kernel_size, kernel_size],
  'MAX', 'VALID', strides=[stride, stride])

tb = tf.cast(ta, tf.float32)
out_avg = tf.nn.pool(tb, [kernel_size, kernel_size],
  'AVG', 'SAME', strides=[stride, stride])

with tf.Session() as sess:
  out_max_np = sess.run(out_max)
  out_avg_np = sess.run(out_avg)

print('origin:')
print(a.reshape((input_size, input_size)))

print('max pooling:')
print(out_max_np.reshape(out_max_np.shape[1:3]))
print('avg pooling:')
print(out_avg_np.reshape(out_avg_np.shape[1:3]))
