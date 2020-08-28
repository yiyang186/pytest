import numpy as np
import cv2

# cap = cv2.VideoCapture('/home/pyy/data/xinke/demo/021.mp4')
# cap = cv2.VideoCapture("/home/pyy/data/cr_demo/christmas2018.mp4")
cap = cv2.VideoCapture("/home/pyy/data/data/大门外.mp4")

# params for ShiTomasi corner detection
maxCorners = 2000
update_freq = 25
moving_th = 1
feature_params = dict( maxCorners = maxCorners, 
                       qualityLevel = 0.01,
                       minDistance = 70,
                       blockSize = 7 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0,255,(maxCorners,3))

# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
# old_gray = old_gray[100:,...]
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)
i = 0

while(1):
    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame_gray = frame_gray[100:,...]

    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    # Select good points
    good_new = p1[st==1]
    good_old = p0[st==1]


    # draw the tracks
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()

        if (a - c) ** 2 + (b - d) ** 2 < moving_th:
            continue

        mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
    # print(frame.shape, mask.shape)
    img = cv2.add(frame,mask)

    cv2.imshow('frame',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)

    if i % update_freq == 0:
      p0 = cv2.goodFeaturesToTrack(frame_gray, mask = None, **feature_params)
      mask = np.zeros_like(frame)
    i += 1


cv2.destroyAllWindows()
cap.release()

