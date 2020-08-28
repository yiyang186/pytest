import tensorflow as tf
from collections import defaultdict
import re

def insert_node_between(new_node, producer_node, consumer_node):
  pass

def node_name_from_input(node_name):
  if node_name.startswith('^'):
    node_name = node_name[1:]
  m = re.search('(.*):\\d+$', node_name)
  if m:
    node_name = m.group(1)
  return node_name

def create_output_node_map(graph_def):
  output_node_map = defaultdict(dict)
  for node in graph_def.node:
    for index, input_name in enumerate(node.input):
      print(input_name)
      input_node_name = node_name_from_input(input_name)
      print(input_node_name)
      output_node_map[input_node_name][node.name] = index
  return output_node_map


g = tf.Graph()
with g.as_default():
  a = tf.constant([1.0], name='a')
  b = tf.constant([2.0], name='b')
  c = tf.add(a, b, name='c')

graph_def = g.as_graph_def()
node_map = {n.name: n for n in graph_def.node}
output_node_map = create_output_node_map(graph_def)
print(output_node_map)

tmp_g = tf.Graph()
with tmp_g.as_default():
  input = tf.placeholder(tf.float32, name='tmp')
  added = tf.constant([3.0])
  new_output = tf.multiply(input, added, name='out')
tmp_g_def = tmp_g.as_graph_def(add_shapes=True) 
tmp_node_map = {n.name: n for n in tmp_g_def.node}
tmp_output_node_map = create_output_node_map(tmp_g_def)
print(tmp_output_node_map)


tmp_index = tmp_output_node_map['tmp']['out']
# del tmp_node_map['out'].input[tmp_index]
# tmp_node_map['out'].input.insert(tmp_index, 'a')
tmp_node_map['out'].input[tmp_index] = 'a'


a_index = output_node_map['a']['c']
del node_map['c'].input[a_index]
node_map['c'].input.insert(a_index, 'out')

for node in tmp_g_def.node:
  if node.op != 'Placeholder':
    graph_def.node.extend([node])

g1 = tf.Graph()
with g1.as_default():
  tf.import_graph_def(graph_def)
tf.summary.FileWriter('events', g1)
