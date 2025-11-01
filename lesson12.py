import cv2

webcam = cv2.VideoCapture(0)
while True: 
 ret,img = webcam.read()
 cv2.imshow('webcam',img)
 k = cv2.waitKey(10)
 if k ==27:
    break


