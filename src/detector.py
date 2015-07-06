#!/usr/bin/python
from sys import argv
import numpy as np
import cv2
import cv2.cv as cv

def detectCircle(imagePath):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.Canny(gray, 32, 2)
    cv2.imwrite("canny.jpg", gray)
    circles = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT, 1, 50, 10, 50, 6, 10)

    if circles is not None:
        circles = np.uint16(np.around(circles)) 
        gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(gray,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(gray,(i[0],i[1]),2,(0,0,255),3)
        cv2.imwrite('circled.jpg', gray)
         
        return len(circles[0])


if __name__ == '__main__':
    if len(argv) < 2:
        exit(1)

    print  detectCircle(argv[1])
