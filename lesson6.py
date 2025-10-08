import cv2
image = cv2.imread("Assets\square.jpg")
# # Gaussian Blur
# blur = cv2.GaussianBlur(image,(7,7),0,0)
# cv2.imshow('blur',blur)
# cv2.waitKey(0)
# # Median Blur - used in digital processing preserves edges but removes noise
# image = cv2.imread("Assets\square.jpg")
# median = cv2.medianBlur(image,5)
# cv2.imshow('median',median)
# cv2.waitKey(0)
# # Bilateral Blur - only sharp edges are preserved here
# image =cv2.imread("Assets\square.jpg")
# bilateral = cv2.bilateralFilter(image,9,75,75)
# cv2.imshow('bilateral',bilateral)
# cv2.waitKey(0)
# Edge Detection in an image
edges = cv2.Canny(image,100,200)
cv2.imshow('edges',edges)
cv2.waitKey(0)
#Rotating an image
image = cv2.imread("Assets\sonic.png")
rotate = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('rotate',rotate)
cv2.waitKey(0)
image = cv2.imread("Assets\sonic.png")
rotate = cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('rotate',rotate)
cv2.waitKey(0)
image = cv2.imread("Assets\sonic.png")
rotate = cv2.rotate(image,cv2.ROTATE_180)
cv2.imshow('rotate',rotate)
cv2.waitKey(0)
# Convert an image from RGB to HSV
hsvImage = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('hsvImage', hsvImage)
cv2.waitKey(0)
