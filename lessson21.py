import cv2
video = cv2.VideoCapture("Assets\cars.mp4")
car_xml = cv2.CascadeClassifier("cars.xml")
while True:
 ret,frames = video.read()
 grayImage = cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
 cars = car_xml.detectMultiScale(grayImage, 1.1,2)
 for (x,y,w,h) in cars:
  cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
 cv2.imshow('video2',frames)
 if cv2.waitKey(33) == 27:
  break

 
