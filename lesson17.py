import cv2,os
haar_file = "facedetector.xml"
datasets = "Datasets\Parish"
# os.chdir (datasets)
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)
Count = 0 
while Count <= 30: 
 ret,img = webcam.read()
# Convert an image from RGB to HSV
 grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 faces = face_cascade.detectMultiScale(grayImage,1.3,4)
 for (x,y,w,h) in faces: 
    cv2.rectangle(img,(x,y),(x + w, y + h),(255,0,0),2)
    face = grayImage[y:y +h, x:x + w]
    face_resize = cv2.resize(face, (100,130))
    os.chdir(datasets)
    cv2.imwrite(f'{Count}.png',face_resize)
 Count += 1
 cv2.imshow('screen',img)
 K = cv2.waitKey(10)
 if K == 27:
        break
