import cv2
import numpy as np
from matplotlib import pyplot as plt

img2 = cv2.imread('myleft.jpg',0)  #queryimage # left image
img1 = cv2.imread('myright.jpg',0) #trainimage # right image

sift = cv2.SIFT()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)


flann = cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1,des2,k=2)
print matches
print len(matches)
good = []
pts1 = []
pts2 = []

# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        good.append(m)
        pts2.append(kp2[m.trainIdx].pt)
        pts1.append(kp1[m.queryIdx].pt)

#Now we have the list of best matches from both the images Lets find the Fundamental Matrix

pts1 = np.asarray(pts1) # ai change ca 
pts2 = np.asarray(pts2)

print len(pts1)
print len(pts2)


F, mask = cv2.findFundamentalMat(pts1,pts2,cv2.FM_LMEDS)


# We select only inlier points
pts1 = pts1[mask.ravel()==1]

pts2 = pts2[mask.ravel()==1]

#Next we find the epilines Epilines corresponding to the points in first image is drawn on second image So mentioning of correct images are important here We get an array of lines So we define a new function to draw these lines on the images

def drawlines(img1,img2,lines,pts1,pts2):
    ''' img1 - image on which we draw the epilines for the points in img2
        lines - corresponding epilines '''
    r,c = img1.shape
    img1 = cv2.cvtColor(img1,cv2.COLOR_GRAY2BGR)
    img2 = cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)
    for r,pt1,pt2 in zip(lines,pts1,pts2):
        color = tuple(np.random.randint(0,255,3).tolist())
        x0,y0 = map(int, [0, -r[2]/r[1] ])
        x1,y1 = map(int, [c, -(r[2]+r[0]*c)/r[1] ])
        
        cv2.line(img1, (x0,y0), (x1,y1), color,1)
        cv2.circle(img1,tuple(pt1.astype('int32')),25,color,-1)
        cv2.circle(img2,tuple(pt2.astype('int32')),25,color,-1)
    return img1,img2

#Now we find the epilines in both the images and draw them.

# Find epilines corresponding to points in right image (second image) and
# drawing its lines on left image


lines1 = cv2.computeCorrespondEpilines(pts2.reshape((-1,1,2)).astype('float32'), 2,F)   # ai ajoute .astype(float)



print "ffffffffffffffffffffffffff"
lines1 = lines1.reshape(-1,3)
img5,img6 = drawlines(img1,img2,lines1,pts1,pts2)   #epilines
print "ggggggggggggggggggggggggggggg"

plt.subplot(121),plt.imshow(img5)
plt.subplot(122),plt.imshow(img6)
plt.show()

# Find epilines corresponding to points in left image (first image) and
# drawing its lines on right image
lines2 = cv2.computeCorrespondEpilines(pts1.reshape(-1,1,2).astype('float32'), 1,F)
print "hhhhhhhhhhhhhhhhhhhhhhhhhhhh"

lines2 = lines2.reshape(-1,3)
img3,img4 = drawlines(img2,img1,lines2,pts2,pts1)

plt.subplot(121),plt.imshow(img5)
plt.subplot(122),plt.imshow(img3)
plt.show()

