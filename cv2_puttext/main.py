import cv2
import numpy as np

FONT = cv2.FONT_HERSHEY_SIMPLEX

img = np.zeros((300, 300, 3), dtype=np.uint8)
h, w, _ = img.shape
cv2.putText(img, '1:fish', (0, h-10), FONT, 2, (13, 77, 255), 5)

cv2.imshow('imshow',img)
cv2.waitKey(0)
