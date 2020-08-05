#!/usr/bin/env python

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
	ret, frame = cap.read()
	if ret==True:
		# Color space coversion
		grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		cv2.imshow('normal',frame)
		cv2.imshow('grayscale',grayscale)
		cv2.imshow('RGB',RGB)
		cv2.imshow('HSV',HSV)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()

