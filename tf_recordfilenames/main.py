import glob
import os
import tensorflow as tf
from tensorflow.contrib import slim

dataset_dir = '/home/pyy/corerain2/data/imagenet/records/cls'
split_name = 'train'
_FILE_PATTERN = 'imagenet_%s-*-*.record'
file_pattern = os.path.join(dataset_dir, _FILE_PATTERN % split_name)

_SPLITS_TO_SIZES = {
    'train': 1281167,
    'val': 50000,
}

_ITEMS_TO_DESCRIPTIONS = {
    'image': 'A color image of varying height and width.',
    'label': 'The label id of the image, integer between 0 and 999',
    'label_text': 'The text of the label.',
    'object/bbox': 'A list of bounding boxes.',
    'object/label': 'A list of labels, one per each object.',
}

_NUM_CLASSES = 1001

g = tf.Graph()
with g.as_default():
  filenames = glob.glob(os.path.join(dataset_dir, 'imagenet_train-*.record'))
  dataset = tf.data.TFRecordDataset(filenames)

  keys_to_features = {
    'name': tf.FixedLenFeature([], tf.string, default_value=''),
    'height': tf.FixedLenFeature([], tf.int64),
    'width': tf.FixedLenFeature([], tf.int64),
    'image': tf.FixedLenFeature((), tf.string, default_value=''),
    'label': tf.FixedLenFeature([], tf.int64),
    'labeltext': tf.FixedLenFeature([], tf.string, default_value=''),
    'format': tf.FixedLenFeature([], tf.string, default_value='raw')
  }
  items_to_handlers = {
      'image': slim.tfexample_decoder.Image('image', 'format'),
      'label': slim.tfexample_decoder.Tensor('label'),
      'height': slim.tfexample_decoder.Tensor('height'),
      'width': slim.tfexample_decoder.Tensor('width'),
      'label_text': slim.tfexample_decoder.Tensor('labeltext'),
  }
  

  decoder = slim.tfexample_decoder.TFExampleDecoder(
      keys_to_features, items_to_handlers)

  dataset = slim.dataset.Dataset(
    data_sources=file_pattern,
    reader=tf.TFRecordReader,
    decoder=decoder,
    num_samples=_SPLITS_TO_SIZES[split_name],
    items_to_descriptions=_ITEMS_TO_DESCRIPTIONS,
    num_classes=_NUM_CLASSES)

  provider = slim.dataset_data_provider.DatasetDataProvider(
    dataset,
    num_readers=16,
    common_queue_capacity=20 * 32,
    common_queue_min=10 * 32)

  [image, label, height, width] = provider.get(['image', 'label', 'height', 'width'])
  image = tf.reshape(image, tf.stack([height, width, 3]))
 
tf.summary.FileWriter('graph', g)
