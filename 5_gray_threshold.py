#!/usr/bin/env python

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
	ret, frame = cap.read()
	if ret==True:
		# Threshold normal and inverse
		grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)		
		ret,normal_thresh = cv2.threshold(grayscale,127,255,cv2.THRESH_BINARY)
		ret,inverse_thresh = cv2.threshold(grayscale,127,255,cv2.THRESH_BINARY_INV)
		adaptiveThreshold = cv2.adaptiveThreshold(grayscale,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

		cv2.imshow('grayscale',grayscale)
		cv2.imshow('normal_thresh',normal_thresh)
		cv2.imshow('inverse_thresh',inverse_thresh)
		cv2.imshow('adaptiveThreshold',adaptiveThreshold)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()

