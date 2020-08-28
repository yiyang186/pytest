# coding:utf-8

import cv2
import numpy as np

gamma = 0.6

img = cv2.imread('./2-1.jpg')
print(float(np.max(img)))
img1 = np.power(img/float(np.max(img)), 1/gamma)
img2 = np.power(img/float(np.max(img)), gamma)

img = cv2.resize(img, (800, 600))
cv2.imshow('src',img)

img1 = cv2.resize(img1, (800, 600))
cv2.imshow('gamma=1/1.5',img1)

img2 = cv2.resize(img2, (800, 600))
cv2.imshow('gamma=1.5',img2)
cv2.waitKey(0)
