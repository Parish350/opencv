import cv2
img1 = cv2.imread("Assets\sonic.png")
print(img1)
cv2.imshow("sonic",img1)
cv2.waitKey(0)

img2 = cv2.imread("Assets\sonic.png",0)
print(img2)
cv2.imshow("sonic",img2)
cv2.waitKey(0)

cv2.imwrite("sonicgrey.png",img2)
img1 = cv2.imread("Assets\sonic.png")
print(img1)
cv2.imshow("sonic",img1)
cv2.waitKey(0)

b,g,r = cv2.split(img1)
cv2.imshow("sonicb",b)
cv2.waitKey(5000)

cv2.imshow("sonicg",g)
cv2.waitKey(5000)

cv2.imshow("sonicr",r)
cv2.waitKey(5000)

cv2.destroyAllWindows()
