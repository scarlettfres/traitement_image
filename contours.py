import cv2
import numpy as np

# create video capture
cap = cv2.VideoCapture(0)


while(1):

	# read the frames
	_,frame = cap.read()

	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	lower_threshold = np.array((118, 41, 0))
	upper_threshold = np.array((140, 255, 255))
	thresh = cv2.inRange(hsv,lower_threshold,upper_threshold)

	thresh = cv2.erode(thresh, cv2.getStructuringElement(cv2.MORPH_ERODE, (3,3) ))
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
	thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
	thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

	contours,hierarchy = cv2.findContours(thresh, 1, 2)
	print contours
	cnt = contours[0]
	M = cv2.moments(cnt)
	epsilon = 0.1*cv2.arcLength(cnt,True)
	approx = cv2.approxPolyDP(cnt,epsilon,False)

	# find contours in the threshold image
	contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	im = cv2.drawContours(frame,contours,0,(0,0,255),2)

	# Show it, if key pressed is 'Esc', exit the loop
	cv2.imshow('frame',frame)
	cv2.imshow('fr',thresh)
	
	if cv2.waitKey(33)== 27:
		break

		# Clean up everything before leaving
		cv2.destroyAllWindows()
		cap.release()


