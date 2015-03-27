import cv2
import cv
global h,s,v,i,im,evente
h,s,v,i,r,g,b,j,evente=0,0,0,0,0,0,0,0,0
#	Mouse callback function	(from earlier mouse_callback.py with little modification)
def my_mouse_callback(event,x,y,flags,param):
	global evente,h,s,v,i,r,g,b,j
	evente=event
	if event==cv.CV_EVENT_LBUTTONDBLCLK:		# Here event is left mouse button double-clicked
		hsv=cv.CreateImage(cv.GetSize(frame),8,3)
		cv.CvtColor(frame,hsv,cv.CV_BGR2HSV)
		(h,s,v,i)=cv.Get2D(hsv,y,x)
		(r,g,b,j)=cv.Get2D(frame,y,x)
		print "x,y =",x,y
		print "hsv= ",cv.Get2D(hsv,y,x)		# Gives you HSV at clicked point
		print "im= ",cv.Get2D(frame,y,x) 	# Gives you RGB at clicked point
	
capture=cv.CaptureFromCAM(0)
frame=cv.QueryFrame(capture)
test=cv.CreateImage(cv.GetSize(frame),8,3)
# 	Now the selection of the desired color from video.( new)
# 	Now the selection of the desired color from video.( new)
cv.NamedWindow("pick")
cv.SetMouseCallback("pick",my_mouse_callback)
while(1):
	frame=cv.QueryFrame(capture)
	cv.ShowImage("pick",frame)
	cv.WaitKey(33)
	if evente==7:					# When double-clicked(i.e. event=7), this window closes and opens next window
		break
cv.DestroyWindow("pick")
