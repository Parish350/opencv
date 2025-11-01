import cv2,os


path =  r"C:\Users\ppuga\Documents\jetlearn\opencv\Assets\images"
os.chdir(path)
images = os.listdir(path)
print(images)
images.sort()

frame = cv2.imread(images[0])
h,w,l = frame.shape
video_name = "MyFirstVideo.avi"
video = cv2.VideoWriter(video_name,0,1,(w,h))
for img in images:
  frame = cv2.imread(img)
  frame = cv2.resize(frame,(w,h))
  video.write(frame)
video.release()

cv2.waitKey(0)
