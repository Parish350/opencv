import cv2
image = cv2.imread("Assets\hishespiderman.png")
#cv2.line(image,(775,986),(0,0),(207,252,3),1)
#cv2.circle(image,(300,200),50,(252,3,3),5)
#cv2.circle(image,(300,200),50,(252,3,3),-1)
#cv2.rectangle(image,(100,100),(50,50),(240,252,3),5)
#cv2.rectangle(image,(100,100),(50,50),(240,252,3),-1)
#cv2.ellipse(image,(250,250),(100,50),30,0,360,(3,252,19),5)
#cv2.ellipse(image,(250,250),(100,50),30,0,360,(3,252,19),-1) 
cv2.imshow('line',image)

cv2.waitKey(0)
