import cv2

def video_demo():
    capture=cv2.VideoCapture(0) 
    if not capture.isOpened():
        print("Can not open camera")

    while(capture.isOpened()):
        ref,frame=capture.read()
 
        cv2.imshow("1",frame)
        c= cv2.waitKey(30) & 0xff 
        if c==27:
            capture.release()
            break
            
video_demo()
cv2.waitKey()
cv2.destroyAllWindows()
