import cv2,os
haar_file = "haarcascade_eye.xml"
datasets = "C:/Users/ppuga\Documents/jetlearn/opencv/Datasets/Parish"
# os.chdir (datasets)
eye_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)
Count = 0 
while Count <= 30: 
 ret,img = webcam.read()
# Convert an image from RGB to HSV
 grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 eyes = eye_cascade.detectMultiScale(grayImage,1.3,4)
 for (x,y,w,h) in eyes: 
    cv2.rectangle(img,(x,y),(x + w, y + h),(255,0,0),2)
    eye = grayImage[y:y +h, x:x + w]
    eye_resize = cv2.resize(eye, (100,130))
    os.chdir(datasets)
    cv2.imwrite(f'{Count}.png',eye_resize)
 Count += 1
 cv2.imshow('screen',img)
 K = cv2.waitKey(10)
 if K == 27:
        break
