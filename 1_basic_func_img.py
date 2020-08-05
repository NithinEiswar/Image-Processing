#!/usr/bin/env python

import numpy as np
import cv2

# Read image
img_gray = cv2.imread('spider.jpeg',0)
img_rgb = cv2.imread('spider.jpeg',1)

# Shape and Type of readed image

print('shape-',img_gray.shape,'type-',type(img_gray))

# Show image
cv2.imshow('spider_0',img_gray)
cv2.imshow('spider_1',img_rgb)

# Flip image
flip_horizontal = cv2.flip(img_rgb,0)
flip_vertical = cv2.flip(img_rgb,1)
flip_both = cv2.flip(img_rgb,-1)

# Write image
cv2.imwrite('flip_horizontal.jpg',flip_horizontal)
cv2.imwrite('flip_vertical.jpg',flip_vertical)
cv2.imwrite('flip_both.jpg',flip_both)

cv2.waitKey(0)
#play with waitKey(0),(1000)
