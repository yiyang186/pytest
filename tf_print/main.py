import tensorflow as tf

a = tf.constant([2])
b = tf.Print(a, [a], 'a:', first_n=10)
c = b + 1

with tf.Session() as sess:
  for i in range(20):
    sess.run(c)

a = tf.constant([2])
b = tf.print(a, [a], 'a:')
tf.add_to_collection('PRINT_OP', b)

print_op = tf.get_collection('PRINT_OP')
print(print_op)
with tf.control_dependencies(print_op):
  b = a + 1

with tf.Session() as sess:
  for i in range(20):
    sess.run(b)
