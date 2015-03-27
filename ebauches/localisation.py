#!/usr/bin/env python

import roslib

import sys
import rospy
import cv
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import cv2
import numpy as np
from matplotlib import pyplot as plt

template = cv2.imread('rect_vert.jpg',1)
w, h,s = template.shape[::-1]
class test_vision_node:

    def __init__(self):
        rospy.init_node('test_vision_node')

        """ Give the OpenCV display window a name. """
        self.cv_window_name = "titre_fenetre"

        """ Create the window and make it re-sizeable (second parameter = 0) """
        cv.NamedWindow(self.cv_window_name, 0)

        """ Create the cv_bridge object """
        self.bridge = CvBridge()

        """ Subscribe to the raw camera image topic """
        self.image_sub = rospy.Subscriber("/usb_cam/image_raw", Image, self.callback)

    def callback(self, data):
        try:
            """ Convert the raw image to OpenCV format """
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            cv_image2=cv.fromarray(cv_image)
            #cv_ptr = cv2.toCvCopy(data,BGR8)
       
            method = eval('cv2.TM_SQDIFF_NORMED')

            # Apply template Matching
            """    result = cv.matchTemplate(gray,patch,cv.TM_CCOEFF_NORMED)
	            result = np.abs(result)**3
	            val, result = cv.threshold(result, 0.01, 0, cv.THRESH_TOZERO)
	            result8 = cv.normalize(result,None,0,255,cv.NORM_MINMAX,cv.CV_8U)
	            cv.imshow("result", result8)"""
            
            
            res = cv2.matchTemplate(cv_image,template,method)
            #cv2.normalize(res,res, 0, 1, 3, -1, Mat() );
            print cv2.minMaxLoc(res)
            #(_, _, minLoc, maxLoc) = cv2.minMaxLoc(result)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            print min_val, max_val, min_loc, max_loc
            top_left = min_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
	    cv2.rectangle(cv_image,top_left, bottom_right, 255, 2)
	    # cv2.Point(top_left, bottom_right)


	    cv.ShowImage(self.cv_window_name, cv_image2)
	    cv.WaitKey(3)
            #template(cv_ptr)
            print "je recois "
            
        except CvBridgeError, e:
            print e
          
          
        

        
    def template(self,img):
    	# All the 6 methods for comparison in a list
	#methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
        #    'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
	method = eval('cv2.TM_SQDIFF_NORMED')

	# Apply template Matching
	res = cv2.matchTemplate(img,template,method)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

	# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		top_left = min_loc
	else:
		top_left = max_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)
	cv2.rectangle(img,top_left, bottom_right, 255, 2)
	plt.subplot(121),plt.imshow(res,cmap = 'gray')
	plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(img,cmap = 'gray')
	plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
	plt.suptitle(meth)

	plt.show()

def main(args):
      vn = test_vision_node()
      try:
        rospy.spin()
      except KeyboardInterrupt:
        print "Shutting down vison node."
      cv.DestroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
    


