from __future__ import print_function
import cv2
import argparse

backSub = cv2.createBackgroundSubtractorKNN()

kernel_size = 3
kernel = (kernel_size,kernel_size)

cap = cv2.VideoCapture(1)

cap.set(3,256)

cap.set(4,192)

while True:
    ret, frame = cap.read()
    if frame is None:
        break

    fgMask = backSub.apply(frame)

    th = cv2.threshold(fgMask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
    th = cv2.erode(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel), iterations=2)
    th = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel), iterations=2)
    contours, hie = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c) > 500:
            (x,y,w,h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y),(x+w,y+h), (255,255,0),2)
        # if x != 0 and y != 0:
        #     print('x',x, 'y',y)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fgMask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break