import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('spider.jpeg',-1)

cv2.imshow('image',img)
img1=cv2.flip(img,-1)
cv2.imwrite('spidy.jpg',img1)
cv2.waitKey(0)              
