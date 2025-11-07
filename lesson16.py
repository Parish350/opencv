import cv2
import numpy as np

webcam = cv2.VideoCapture(0)
for i in range(60):
  return_val,background = webcam.read()
while True: 
 ret,img = webcam.read()
# Convert an image from RGB to HSV
 hsvImage = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
 lower_red = np.array([0, 120, 70]) # light red
 upper_red = np.array([10, 255, 255]) # bright red
 mask = cv2.inRange(hsvImage,lower_red,upper_red)
 mask2 = cv2.bitwise_not(mask)
 result1 = cv2.bitwise_and(background,background,mask = mask)
 result2 = cv2.bitwise_and(img,img,mask = mask2)
 final = cv2.addWeighted(result1,1,result2,1,0)
 cv2.imshow('webcam',final)
 k = cv2.waitKey(10)
 if k ==27:
    break
