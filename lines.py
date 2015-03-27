
import math
import cv2
import numpy as np

img = cv2.imread('my_photo-4.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

#line = cv2.HoughLines(edges,1,np.pi/90,200)
line = cv2.HoughLinesP(edges, 1, math.pi/180, 20, None, 10, 10 )
for l in range(len(line[0])):
        cv2.line(img, (line[0][l][0],line[0][l][1]), (line[0][l][2],line[0][l][3]),(0,0,255),2)

cv2.imwrite('houghlines3.jpg',img)
cv2.imwrite('houghfrff.jpg',edges)


