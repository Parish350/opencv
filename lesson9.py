import cv2
import numpy as np
# image = cv2.imread("Assets\ghost.png")
# gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# gray_blurred = cv2.blur(gray,(3,3))
# detected_circles = cv2.HoughCircles(gray_blurred,cv2.HOUGH_GRADIENT,1,20,param1 = 50, param2 = 30, minRadius=1, maxRadius = 100, )
# print(detected_circles)

# detected_circles = np.uint16(np.around(detected_circles)) 
# for pt in detected_circles[0,:]:
#     x,y,r = pt[0],pt[1],pt[2]
#     cv2.circle(image,(x,y),r,(207,252,3),1)
# cv2.imshow('circles',image)
# cv2.waitKey(0)
image = cv2.imread("Assets\Blobs.jpeg")
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 100
params.filterByCircularity = True
params.minCircularity = 0.1
params.maxCircularity = 0.8
params.filterByConvexity = True
params.minConvexity = 0.2
params.filterByInertia = True
params.minInertiaRatio = 0.01
detector = cv2.SimpleBlobDetector_create(params)
blobs = detector.detect(image)
img1 = cv2.drawKeypoints(image, blobs,None,(0,0,255),cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)  


cv2.imshow('blobs',img1)
cv2.waitKey(0)
