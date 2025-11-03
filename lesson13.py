import cv2,os


path =  r"C:\Users\ppuga\Documents\jetlearn\opencv\pictures"
os.chdir(path)
image = os.listdir(path)
images = []

for img in image:
  if img.endswith(('.jpg','.jpeg','.png')):
   images.append(img)
print(image)
images.sort()

frame = cv2.imread(images[0])
h,w,l = frame.shape
video_name = "MySecondVideo.avi"
video = cv2.VideoWriter(video_name,0,1,(w,h))
for img in images:
  frame = cv2.imread(img)
  frame = cv2.resize(frame,(w,h))
  video.write(frame)
video.release()

cv2.waitKey(0)
