import cv2,os


path =  r"C:\Users\ppuga\Documents\jetlearn\opencv\Assets\images"
os.chdir(path)
images = os.listdir(path)
print(images)
images.sort()

frame = cv2.imread(images[0])

cv2.waitKey(0)
