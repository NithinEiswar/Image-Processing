#!/usr/bin/env python

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
	# similar to imread()
	ret, frame = cap.read()
	# ret tells whether we got any input or not
	if ret==True:
		out.write(frame)
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
# close all windows and release video capture and saver
cap.release()
out.release()
cv2.destroyAllWindows()
