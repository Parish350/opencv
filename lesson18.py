import cv2
import cv2,numpy,os
haar_file = "facedetector.xml"
datasets = 'Datasets'
(images,labels,names,id) = ([],[],{},0)
for (subdirs,dirs,files)in os.walk(datasets):
 for subdir in dirs:
  names[id] = subdir
  subjectpath = os.path.join(datasets,subdir)
  for filename in os.listdir(subjectpath):
   path = subjectpath +'/'+ filename
   images.append(cv2.imread(path,0))
   label = id
   labels.append(int(label))
  id += 1
#(images,labels) = [numpy.array(list)for list in[images,labels]]
# print(images)
# for i,img in enumerate(images):
#  print(i,img.shape)

images = numpy.array(images)
labels = numpy.array(labels)
recoginser = cv2.face.LBPHFaceRecognizer_create()
recoginser.train(images,labels)
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)
while True: 
 ret,img = webcam.read()
# Convert an image from RGB to HSV
 grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 faces = face_cascade.detectMultiScale(grayImage,1.3,4)
 for (x,y,w,h) in faces: 
    cv2.rectangle(img,(x,y),(x + w, y + h),(255,0,0),2)
    face = grayImage[y:y +h, x:x + w]
    face_resize = cv2.resize(face, (100,130))
    prediction = recoginser.predict(face_resize)
    print(prediction)
    if prediction[1]>60:
      cv2.putText(img,f'{names[prediction[0]]}',(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0))
 cv2.imshow('screen',img)
 K = cv2.waitKey(10)
 if K == 27:
        break
