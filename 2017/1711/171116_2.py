# cnn_model_reduced
import pickle
import numpy as np
import tensorflow as tf
from math import sqrt
import pandas as pd

def unpickle(file):
    with open(file, 'rb') as fo:
        data = pickle.load(fo, encoding='bytes')
    return data

def load_CIFAR10(pos, n_chunks=1):
    Xtr = []
    Ytr = []
    for i in range(n_chunks):
        train = unpickle(pos + '/data_batch_{0}'.format(i + 1))
        Xtr.extend(train[b'data'])
        Ytr.extend(train[b'labels'])
    test = unpickle(pos + '/test_batch')
    Xte = test[b'data']
    Yte = test[b'labels']
    return np.array(Xtr), np.array(Ytr), np.array(Xte), np.array(Yte)

def onehot_encoding (Ytr, Yte):
    Ytr_onehot = np.eye(10)[Ytr]
    Yte_onehot = np.eye(10)[Yte]
    return Ytr_onehot, Yte_onehot

class CNN:
    def __init__(self, sess, beta, gamma, n_row, batch_size):
        self.sess = sess
        self.beta = beta
        self.gamma = gamma
        self.batch_size = batch_size
        self.n_row = n_row
        self.X = tf.placeholder(tf.float32, [None, 32, 32, 3])
        self.Y = tf.placeholder(tf.float32, [None, 10])
    def modeling(self, optimizer):
        L1 = self.model(self.X, 7, 3, 64, 2, 'Layer_1') # 16*16
        L1_identity = self.pooling(L1, 3) # 8*8
        L2_1 = self.model(L1_identity, 1, 64, 64, 1, 'Layer_2_1', pad='VALID')
        L2_2 = self.model(L2_1, 3, 64, 64, 1, 'Layer_2_2')
        L2_3 = self.model(L2_2, 1, 64, 256, 1, 'Layer_2_3', pad='VALID') 
        L2_4 = self.model(L1_identity, 1, 64, 256, 1, 'Layer_2_4', pad='VALID')
        L2 = tf.nn.relu(L2_3 + L2_4)
        L3_1 = self.model(L2, 1, 256, 64, 1, 'Layer_3_1', pad='VALID')
        L3_2 = self.model(L3_1, 3, 64, 64, 1, 'Layer_3_2')
        L3_3 = self.model(L3_2, 1, 64, 256, 1, 'Layer_3_3', pad='VALID')
        L3 = tf.nn.relu(L2 + L3_3)
        L4_1 = self.model(L3, 1, 256, 64, 1, 'Layer_4_1', pad='VALID')
        L4_2 = self.model(L4_1, 3, 64, 64, 1, 'Layer_4_2')
        L4_3 = self.model(L4_2, 1, 64, 256, 1, 'Layer_4_3', pad='VALID')
        L4 = tf.nn.relu(L3 + L4_3)
        L5_1 = self.model(L4, 1, 256, 128, 2, 'Layer_5_1', pad='VALID')
        L5_2 = self.model(L5_1, 3, 128, 128, 1, 'Layer_5_2')
        L5_3 = self.model(L5_2, 1, 128, 512, 1, 'Layer_5_3', pad='VALID')
        L5_identity = self.model(L4, 1, 256, 512, 2, 'Layer_5_identity', pad='VALID') # 4*4
        L5 = tf.nn.relu(L5_identity + L5_3)
        # L6_1 = self.model(L5, 1, 512, 128, 1, 'Layer_6_1', pad='VALID')
        # L6_2 = self.model(L6_1, 3, 128, 128, 1, 'Layer_6_2')
        # L6_3 = self.model(L6_2, 1, 128, 512, 1, 'Layer_6_3', pad='VALID')
        # L6 = tf.nn.relu(L5 + L6_3)
        # L7_1 = self.model(L6, 1, 512, 128, 1, 'Layer_7_1', pad='VALID')
        # L7_2 = self.model(L7_1, 3, 128, 128, 1, 'Layer_7_2')
        # L7_3 = self.model(L7_2, 1, 128, 512, 1, 'Layer_7_3', pad='VALID')
        # L7 = tf.nn.relu(L6 + L7_3)
        # L8_1 = self.model(L7, 1, 512, 128, 1, 'Layer_8_1', pad='VALID')
        # L8_2 = self.model(L7_1, 3, 128, 128, 1, 'Layer_8_2')
        # L8_3 = self.model(L7_2, 1, 128, 512, 1, 'Layer_8_3', pad='VALID')
        # L8 = tf.nn.relu(L7 + L8_3)
        # L9_1 = self.model(L8, 1, 512, 256, 2, 'Layer_9_1', pad='VALID')
        # L9_2 = self.model(L9_1, 3, 256, 256, 1, 'Layer_9_2')
        # L9_3 = self.model(L9_2, 1, 256, 1024, 1, 'Layer_9_3', pad='VALID')
        # L9_identity = self.model(L8, 1, 512, 1024, 2, 'Layer_9_identity', pad='VALID') # 2*2
        # L9 = tf.nn.relu(L9_identity + L9_3)

        model_ = self.pooling(L5, 4, type='avg')
        model_ = tf.reshape(model_, [-1, 512])
        W = tf.Variable(tf.random_normal([512, 10], stddev=sqrt(4/522)), name='fully-connected')
        self.model_ = tf.matmul(model_, W)
        self.loss_funtion(self.Y, optimizer)

    def _batch(self, iterable, length, n=1):
        for ndx in range(0, length, n):
            yield iterable[ndx:min(ndx + n, length)]
    def train(self, X, y, n_epoch):
        n_row, sess, batch_size = self.n_row, self.sess, self.batch_size
        for epoch in range(n_epoch):
            # n = 1
            arr = np.random.randint(n_row, size=n_row)
            for x in self._batch(range(n_row), n_row, batch_size):
                batch_X, batch_y = X[arr[x], :], y[arr[x]]
                loss_, _ = sess.run([self.loss, self.optimizer], feed_dict={self.X:batch_X, self.Y:batch_y})
                # if n % 100 == 0:
                #     print('epoch: %d, step: %d\nloss: %f\n' %(epoch, n, loss_))
                # n += 1
    def predict(self, Xte, Yte, n_row):
        sess = self.sess
        cor_ = 0
        arr = np.arange(n_row)
        for x in self._batch(range(n_row), n_row, 200):
            X_, y_ = Xte[arr[x], :], Yte[arr[x]]
            correct = self.metric(y_)
            cor = sess.run(correct, {self.X:X_})
            cor_ += cor
        return cor_ / n_row
    def metric(self, Yte):
        model_ = self.model_
        correct = tf.equal(tf.argmax(model_, 1), tf.argmax(Yte,1))
        correct = tf.reduce_sum(tf.cast(correct, tf.float32))
        return correct
    def loss_funtion(self, y, optimizer):
        model= self.model_
        global_step = tf.Variable(0, trainable=False)
        learning_rate = tf.train.exponential_decay(0.1, global_step, 2000, 0.1)
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=model, labels=y))
        if optimizer == 'adam':
            self.optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss, global_step=global_step)
        elif optimizer == 'sgd':
            self.optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss, global_step=global_step)
        self.loss = loss
    def model(self, X, filter_size, in_feature, out_feature, stride, name, pad = 'SAME'):
        beta, gamma = self.beta, self.gamma
        std = sqrt(4/(in_feature + out_feature))
        with tf.variable_scope(name):
            W = tf.Variable(tf.random_normal([filter_size, filter_size, in_feature, out_feature], stddev=std))
            L = tf.nn.conv2d(X, W, strides=[1,stride,stride,1], padding=pad)
            L = tf.nn.relu(L)
            mean, var = self.mean_var(L)
            L = tf.nn.batch_normalization(L, offset=beta, scale=gamma, mean=mean, variance=var, variance_epsilon=1e-3)
        return L
    def mean_var(self, X):
        mean = tf.reduce_mean(X, axis=0)
        var = tf.reduce_mean((X-mean)**2, axis=0)
        return mean, var
    def pooling(self, L, ksize, type='max'):
        if type == 'max':
            L = tf.nn.max_pool(L, ksize=[1, ksize, ksize, 1], strides=[1, ksize-1, ksize-1, 1], padding='SAME')
        else:
            L = tf.nn.avg_pool(L, ksize=[1, ksize, ksize, 1], strides=[1, ksize, ksize, 1], padding='VALID')
        return L
    def save_model(self, sess, i):
        saver = tf.train.Saver()
        saver.save(sess, './save_model_reduced/cnn_model_reduced_{}.ckpt'.format(i))

if __name__ == '__main__':
    Xtr, Ytr, Xte, Yte = load_CIFAR10('cifar-10-batches-py', 5)                             
    Xtr = Xtr.reshape(50000, 3, 32, 32).transpose(0,2,3,1).astype("float")
    Xte= Xte.reshape(10000, 3, 32, 32).transpose(0,2,3,1).astype("float")
    Ytr, Yte = onehot_encoding(Ytr, Yte)

    # beta, gamma = 0.1, 0.211
    n_row, batch_size = 50000, 200
    n_epoch = 20
    # with tf.Session() as sess:
    #     res = CNN(sess, beta, gamma, n_row, batch_size)
    #     res.modeling('adam')
    #     sess.run(tf.global_variables_initializer())
    #     res.train(Xtr, Ytr, n_epoch)
    #     print('#'*30)
    #     print('Accuracy:', res.predict(Xte, Yte, 10000))
    #     print('#'*30)
    # quit()
    grid = pd.DataFrame(columns=['beta', 'gamma', 'optimizer', 'Accuracy'])
    n = 0
    for op in ['adam', 'sgd']:
        for b in [0.1*i for i in range(1, 10)]:
            for g in [0.1*j for j in range(1, 10)]:
                with tf.Session() as sess:
                    res = CNN(sess, b, g, n_row, batch_size)
                    res.modeling(op)
                    sess.run(tf.global_variables_initializer())
                    res.train(Xtr, Ytr, n_epoch)
                    res.save_model(sess, n)
                    acc = res.predict(Xte, Yte, 10000)
                    grid.loc[n] = [b, g, op, acc]
                    grid.to_csv('cnn_performance_reduced.csv')
                    print('epoch: %d\nop: %s\nbeta: %f\ngamma: %f\n' %(n, op, b, g))
                    n += 1