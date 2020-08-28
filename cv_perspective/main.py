import cv2
import numpy as np
import random

img = cv2.imread('./tailbridge_101.jpg')
h, w, _ = img.shape
ratios = [0, 0, 0, 0]
ratios[random.choice(range(4))] = random.uniform(0, 0.2)

# 4 points: left-top, left-bottom, right-bottom, right-top
origin_points = np.array(
    [[0, 0],[0, h],[w, h],[w, 0]],dtype = "float32")
transformed_points = np.array(
    [[ratios[1] * w, ratios[0] * h],
    [ratios[2] * w, (1 - ratios[0]) * h],
    [(1 - ratios[2]) * w, (1 - ratios[3]) * h],
    [(1 - ratios[1]) * w, ratios[3] * h]], dtype="float32")
M = cv2.getPerspectiveTransform(origin_points, transformed_points)
out_img = cv2.warpPerspective(img, M, (w, h))
out_img = cv2.resize(out_img, (800, 600))
cv2.imshow("img",out_img)
cv2.waitKey(0)
