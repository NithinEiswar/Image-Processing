#!/usr/bin/env python

import numpy as np
import cv2

# Read image
ironman = cv2.imread('ironman.jpg')
ironman_org = cv2.imread('ironman.jpg')
thanos = cv2.imread('thanos.png')

cap = cv2.imread('cap.jpg')


cv2.imshow('marvel',ironman)
cv2.waitKey(2000)
cv2.imshow('marvel',thanos)
cv2.waitKey(2000)
cv2.imshow('marvel',cap)
cv2.waitKey(2000)

# Resize image to required dimension
thanos = cv2.resize(thanos,(330,405))
cap = cv2.resize(cap,(230,405))

#		Y-axis,  X-axis
ironman[0:405 , 235:565] = thanos
ironman[0:405 , 568:798] = cap

ironman = cv2.line(ironman,(235,0),(565,405),(255,0,0),5)
ironman = cv2.rectangle(ironman,(235,0),(565,405),(0,255,0),10)
ironman = cv2.circle(ironman,(400,100), 63, (0,0,255), -1)
																# Font scale, Color,   Thickness,
cv2.putText(ironman,'ENDGAME',(250,50), cv2.FONT_HERSHEY_SIMPLEX,    2,		(255,0,0),	   4,		cv2.LINE_AA)

cv2.imshow('ironman',ironman)
cv2.waitKey(0)

# Addition, Subtraction, Weighted addition
ironman = ironman_org[0:405 , 235:565]
ironman = cv2.resize(ironman,(230,405))
addition = cv2.add(ironman,cap)
# we dont need to use cv2.add(), we can directly add both images
subtraction = ironman-cap

# ðﾝﾑﾑðﾝﾑﾠðﾝﾑﾡ = ðﾝﾛﾼ · ðﾝﾑﾖðﾝﾑﾚðﾝﾑﾔ1 + ðﾝﾛﾽ · ðﾝﾑﾖðﾝﾑﾚðﾝﾑﾔ2 + gamma( value - 0) --> bias kind of thing
weighted_add = cv2.addWeighted(ironman,0.5,cap,0.5,0)

cv2.imshow('subtraction',subtraction)
cv2.waitKey(0)
cv2.imshow('addition',addition)
cv2.waitKey(2000)
cv2.imshow('weighted_add',weighted_add)
cv2.waitKey(0)

#cv2.imshow('ironman',ironman)
#cv2.waitKey(0)
