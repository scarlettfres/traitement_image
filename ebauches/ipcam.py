import numpy as np
import cv2


cap = cv2.VideoCapture()
opened=cap.open("http://root:fakeshop_pepper@10.0.161.201/view/viewer_index.shtml?id=87\?dummy=video.mjpg")
	#rtsp://username:passwordp@IpAddress:554/axis-media/media.amp
	#"http://USER:PWD@IPADDRESS:8088/mjpeg.cgi?user=USERNAME&password=PWD&channel=0&.mjpg";*/ 
	
print opened
#print cap
ret, frame = cap.read()
print frame, ret
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
   
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
  # cv2.imshow('frame',gray)
   # if cv2.waitKey(1) & 0xFF == ord('q'):
       # break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

