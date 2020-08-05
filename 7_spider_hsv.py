#!/usr/bin/env python

import cv2
import numpy as np

img = cv2.imread("rgb_circle.png")

blur = cv2.blur(img,(5,5))
cv2.imshow("blur", blur)
cv2.waitKey(0)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# RGB HSV Range
lower_red = np.array([170, 70, 50])
upper_red = np.array([180, 255, 255])
lower_green = np.array([50,120,120])
upper_green = np.array([80,255,255])
lower_blue = np.array([83,120,120])
upper_blue = np.array([170,255,255])

# HSV Thresholding
mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

'''
cv2.imshow("BGR Image", img)
cv2.imshow("HSV Image", hsv)
cv2.imshow("Red", mask_red)
cv2.imshow("Green", mask_green)
cv2.imshow("Blue", mask_blue)
cv2.waitKey(0)
'''

# Contours
image, contours, hierarchy = cv2.findContours(mask_red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours_draw = cv2.drawContours(img, contours, -1, (0,255,0), 3)

x,y,w,h = cv2.boundingRect(contours[0])
img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

cnt = contours[0]
M = cv2.moments(cnt)
# Centroid calculation
cx,cy = int(M['m10']/M['m00']),int(M['m01']/M['m00'])
# Area calculation
area = cv2.contourArea(cnt)

print('centre-',(cx,cy), 'Area-',area)
cv2.imshow("contours_draw", contours_draw)
cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
