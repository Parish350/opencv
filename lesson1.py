# import cv2
# img1 = cv2.imread("Assets\pika.png")
# print(img1)
# cv2.imshow("pika",img1)
# cv2.waitKey(0)

# img2 = cv2.imread("Assets\pika.png",0)
# print(img2)
# cv2.imshow("pika",img2)
# cv2.waitKey(0)

# cv2.imwrite("pikagrey.png",img2)
import cv2
img1 = cv2.imread("Assets\opencv.png")
print (img1)
cv2.imshow("opencv",img1)
cv2.waitKey(0)

img2 = cv2.imread("Assets\opencv.png",0)
print (img2)
cv2.imshow("opencv",img2)
cv2.waitKey(0)

cv2.imwrite("opencv.png",img2)
b,g,r = cv2.split(img1)
cv2.imshow("opencvb",b)
cv2.waitKey(0)

cv2.imshow("opencvg",g)
cv2.waitKey(0)

cv2.imshow("opencvr",r)
cv2.waitKey(0)
img1 = cv2.imread("Assets\pika.png")
print(img1)
cv2.imshow("pika",img1)
cv2.waitKey(0)

b,g,r = cv2.split(img1)
cv2.imshow("pikab",b)
cv2.waitKey(5000)

cv2.imshow("pikag",g)
cv2.waitKey(5000)

cv2.imshow("pikar",r)
cv2.waitKey(5000)

cv2.destroyAllWindows()
