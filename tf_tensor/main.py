import tensorflow as tf

g = tf.Graph()
with g.as_default():
  a = tf.constant(1)
  b = tf.constant(2)
  c = a + b
  d = a - b

ops = g.get_operations()

ts = []
for op in ops:
  ts += op.outputs

for t in set(ts):
  print(t.name, t.op.name, t.value_index, t.consumers()) # t.op
