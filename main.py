import cv2
import numpy as np
import tensorflow as tf


im = cv2.imread('img/test.jpg',1)
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

"""
cv2.namedWindow("Colorfull image",cv2.WINDOW_NORMAL)
cv2.namedWindow("Gray image",cv2.WINDOW_NORMAL)
cv2.imshow("Colorfull image",im)
cv2.imshow("Gray image",img)
cv2.waitKey(0)




#######----- Convolutional Network Implementation -----########
"""
sess = tf.Session()

x = tf.placeholder(tf.float32, shape=[None, 576])
y_ = tf.placeholder(tf.float32, shape=[None, 2])

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def biases_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W, b, w, h, c):
    return tf.nn.conv2d(x, W, strides=[b, w, h, c], padding='SAME')

x_image = tf.reshape(x, [-1, 24, 24, 1],)

wA_conv1 = weight_variable([9, 9, 1, 48])
bA_conv1 = biases_variable([48])

s = tf.shape(wA_conv1)

wB_conv1 = weight_variable([9, 9, 1, 48])
bB_conv1 = biases_variable([48])

hA_conv1 = conv2d(x_image, wA_conv1, 1, 9, 9, 1) + bA_conv1
hB_conv1 = (conv2d(x_image, wB_conv1, 1, 9, 9, 1))+ bB_conv1
h_conv1 = maxout(hA_conv1, hB_conv1)
