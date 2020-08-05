#!/usr/bin/env python

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
	ret, frame = cap.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	equ = cv2.equalizeHist(frame)
	if ret==True:
		cv2.imshow('frame',frame)
		cv2.imshow('equ',equ)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
# close all windows and release video capture and saver
cap.release()
cv2.destroyAllWindows()