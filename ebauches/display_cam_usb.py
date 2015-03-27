import base64
import time
import urllib2
import numpy as np
import cv2



class ipCamera(object):
 
	def __init__(self, url, user, password):
		self.url = url
		auth_encoded = base64.encodestring('%s:%s' % (user, password))[:-1]
		 
		self.req = urllib2.Request(self.url)
		print "aaaaaaa"
		print self.req
		self.req.add_header('Authorization', 'Basic %s' % auth_encoded)
		 
	def get_frame(self):
		response = urllib2.urlopen(self.req)
		img_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
		frame = cv2.imdecode(img_array, 1)
		return frame 


class Camera(object):
 
	def __init__(self, camera=0):
		#self.cam = cv2.VideoCapture(camera)
		self.cam = cv2.VideoCapture("rtsp://root:fakeshop_pepper@10.0.161.201:3128/axis-media/media.amp")
		if not self.cam:
			raise Exception("Camera not accessible")
		 
		self.shape = self.get_frame().shape
	 
	def get_frame(self):
		_, frame = self.cam.read()
		return frame 


if __name__ == '__main__':
	
	#ipcam=ipCamera("http://10.0.161.201","root","fakeshop_pepper")
    	#frame=ipcam.get_frame()
    	cam=Camera()	
	while(True):
	
		#frame=cam.get_frame()	# camera usb	
		frame=ipcam.get_frame()	#camera IP
	
		print frame
		#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Display 
		cv2.imshow('frame',gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

		# release the capture at the end
	cap.release()
	cv2.destroyAllWindows()

