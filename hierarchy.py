#!/usr/bin/env python

import cv2
import numpy as np

img = cv2.imread("boxes.jpg")
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,normal_thresh = cv2.threshold(grayscale,127,255,cv2.THRESH_BINARY)

image, contours, hierarchy = cv2.findContours(normal_thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(len(contours),contours)
req_img = cv2.drawContours(img, contours[1], -1, (0,255,0), 10)	

cv2.imshow("req_img", req_img)
cv2.waitKey(0)

print(hierarchy)

cv2.imshow("normal_thresh", normal_thresh)
cv2.waitKey(0)