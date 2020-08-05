#!/usr/bin/env python

import numpy as np
import cv2

black_img = np.zeros((600,800,1), np.uint8)
white_img = np.zeros((600,800,1), np.uint8)
white_img[:,:] = 255
gray_img = np.zeros((600,800,1), np.uint8)
gray_img[:,:] = 127

'''
cv2.imshow('black_img',black_img)
cv2.waitKey(2000)
cv2.imshow('white_img',white_img)
cv2.waitKey(2000)
cv2.imshow('gray_img',gray_img)
cv2.waitKey(2000)
'''

# Inverse
inverse_white = cv2.bitwise_not(white_img)
#cv2.imshow('inverse_blk',inverse_blk)
#cv2.waitKey(2000)

# Bitwise AND
B_and_W = cv2.bitwise_and(gray_img, gray_img, mask = black_img)
#cv2.imshow('B_and_W',B_and_W)
#cv2.waitKey(2000)s