import tensorflow as tf
from tensorflow.core.framework import graph_pb2
from tensorflow.core.framework import node_def_pb2

def replace_graph(graphdef):
  tf.reset_default_graph()
  g = tf.get_default_graph()
  with g.as_default():
    tf.import_graph_def(graphdef)

def remove_ops(remove_ops):
  graph = tf.get_default_graph()
  gd = graph.as_graph_def()
  nodes = [d.node_def for d in remove_ops]

  ngd = graph_pb2.GraphDef()
  ngd.node.extend(nodes)
  return replace_graph(ngd)


a = tf.constant(1, name='a')
b = tf.constant(2, name='b')
c = tf.add(a, b, name='c')

d = tf.constant(1, name='d')
e = tf.constant(2, name='e')
f = tf.add(d, e, name='f')


nodes = [d.op, e.op, f.op]
remove_ops(nodes)

g = tf.get_default_graph()
tf.summary.FileWriter('.', g)

print(g.get_tensor_by_name('w:0'))
