import tensorflow as tf


logits = tf.constant([[0, 1],
                      [1, 1],
                      [2, -4]], dtype=tf.float32)
y_true = tf.constant([[1, 1],
                      [1, 0],
                      [1, 0]], dtype=tf.float32)
# tensorflow api
loss = tf.losses.sigmoid_cross_entropy(multi_class_labels=y_true,
                                       logits=logits)

# manul computing
probs = tf.nn.sigmoid(logits)
loss_t = tf.reduce_mean(y_true * (-tf.log(probs)) +
                        (1 - y_true) * (-tf.log(1 - probs)))

config = tf.ConfigProto()
config.gpu_options.allow_growth = True  # pylint: disable=no-member
with tf.Session(config=config) as sess:
    loss_ = loss.eval()
    loss_t_ = loss_t.eval()
    print('sigmoid_cross_entropy: {: .3f}\nmanual computing: {: .3f}'.format(
        loss_, loss_t_))
