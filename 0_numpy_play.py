#!/usr/bin/env python

import cv2
import numpy as np   #assigning the name np to numpy 

a = np.zeros((5,5))  #Creates array of all zeros of shape 5x5 
b = np.ones((4,4))      #Creates array of all ones of shape 4x4
c = np.random.randint(20,size =(15,15))    #Creates a random 2D array of integers (between 0 to 19) of shape 15 x 15

t = np.transpose(c,(2, 0 ,1))              #do transpose operation on the array c
ba = np.bitwise_and(c > 3, c < 9)

print("From 3rd column: ")
print(c[:,3:])                             #prints the Output columns from 3 to last column

print("From 3rd row: ")
print(c[2:,:])                              #prints the Output starting from third row of array

print(a)             #prints the created array
