#http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html
import numpy as np
import cv2

cap = cv2.VideoCapture('MOV_0144_1.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
