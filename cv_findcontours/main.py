import numpy as np
import cv2

img = np.zeros((600, 600, 3), dtype=np.uint8)
img += 255

img[100:150, 100:150, :] = 1
img[130:180, 130:180, :] = 1

img[400:550, 400:550, :] = 2
img[100:150, 400:550, :] = 2

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
binary, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
  print(contour.tolist())

cv2.drawContours(img, contours[1:], -1, (0, 0, 255), 3)
cv2.imshow('img', img)
cv2.waitKey(0)
