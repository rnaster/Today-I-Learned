import tensorflow as tf
import numpy as np
import pandas as pd
from itertools import islice

config = tf.ConfigProto(allow_soft_placement=True)
config.gpu_options.allocator_type = 'BFC'
config.gpu_options.per_process_gpu_memory_fraction = 0.9

train = pd.read_csv('train.csv')
# print(train.head())
train_X, train_y = train.drop('Class', axis=1), train.Class
train_X = train_X.as_matrix()
train_y = train_y.as_matrix()

valid = pd.read_csv('valid.csv')
cv_X, cv_y = valid.drop('Class', axis=1), valid.Class
cv_X, cv_y = cv_X.as_matrix(), cv_y.as_matrix()

col = 30
row = len(train_X)
X = tf.placeholder(shape=[None, col], dtype=tf.float32)
y_ = tf.placeholder(shape=[None,], dtype=tf.float32)

W = tf.Variable(tf.random_uniform(shape=[col, 1], minval=-1, maxval=1), name='weight')
b = tf.Variable(tf.random_uniform(shape=[1, 1], minval=-1, maxval=1), name='bias')
z = tf.matmul(X, W) + b
y = tf.sigmoid(z)
epsilon = 1e-6
loss = -tf.reduce_mean((1-y_)*tf.log(1-y+epsilon) + y_*tf.log(y+epsilon))
# loss = tf.reduce_sum(cross_entropy)*(1/row)

threshold = 0.95
pred = tf.cast(tf.greater(y, threshold), tf.float32)
conf_mtx = tf.confusion_matrix(y_, pred)

re_help = tf.reduce_sum(tf.gather_nd(conf_mtx, [[1, 0], [1, 1]]))
if re_help !=0:
	re = tf.gather_nd(conf_mtx, [1, 1]) / re_help
else:
	re = 0

pre_help = tf.reduce_sum(tf.gather_nd(conf_mtx, [[0, 1], [1, 1]]))
if pre_help !=0:
	pre = tf.gather_nd(conf_mtx, [1, 1]) / pre_help
else:
	pre = 0

f1 = 2*pre*re / (re + pre) if pre != 0 and re != 0 else 0

learning_rate = 0.01
training_op = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)

# f1_score = 0
def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())
n_epoch = 50
batch_size = 100
idx = list(chunk(range(row), batch_size))
with tf.Session() as sess:
	init = tf.global_variables_initializer()
	sess.run(init)
	# print(sess.run(tf.shape(y), feed_dict={X:train_X, y_:train_y}))
	# print(sess.run(tf.reduce_sum(pred), feed_dict={X:train_X, y_:train_y}), '**')
	# print(a)
	# print(sess.run(loss, feed_dict={X:train_X[:300, :], y_:train_y[:300]}))
	# print(sess.run(tf.shape(loss), feed_dict={X:train_X[:300,], y_:train_y[:300]}))
	# print(sess.run([re, pre, pre_help, f1], feed_dict={X:cv_X, y_:cv_y}), '#'*60)
	# quit()
	for epoch in range(n_epoch):
		for step in range(0, row//batch_size-1):
			# batch_X, batch_y = train_X[batch_size*(step-1):batch_size*step, :], train_y[batch_size*(step-1):batch_size*step]
			# print(step)
			index = list(idx[step])
			loss_, _ = sess.run([loss, training_op], feed_dict={X:train_X[index, :], y_:train_y[index]})		
			print('loss:', loss_, 'step:',step)
			f1_ = sess.run(f1, feed_dict={X:cv_X[:100, :], y_:cv_y[:100]})
			print('f1_score:', f1_)
		