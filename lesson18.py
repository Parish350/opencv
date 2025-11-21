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
print(images)
for i,img in enumerate(images):
 print(i,img.shape)
 
images = numpy.array(images)
labels = numpy.array(labels)
recoginser = cv2.face.LBPHFaceRecognizer_create()
recoginser.train(images,labels)
