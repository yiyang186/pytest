import math
import numpy as np

def softmax(x):
  return np.exp(x) / np.sum(np.exp(x))

def sigmoid(x):
  return 1. / (1. + np.exp(-x))


a = np.array([0.5, 0.6])
print(softmax(a))
print(sigmoid(a))

a = np.array([1.5, 1.6])
print(softmax(a))
print(sigmoid(a))

a = np.array([1.5, 2.6])
print(softmax(a))
print(sigmoid(a))

a = np.array([.5, 2.6])
print(softmax(a))
print(sigmoid(a))
