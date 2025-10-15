import cv2
import numpy as np
image = cv2.imread("Assets\Tails.png")
#cv2.line(image,(624,722),(0,0),(207,252,3),1)
#cv2.circle(image,(300,200),50,(252,3,3),5)
#cv2.circle(image,(300,200),50,(252,3,3),-1)
#cv2.rectangle(image,(100,100),(50,50),(240,252,3),5)
#cv2.rectangle(image,(100,100),(50,50),(240,252,3),-1)
#cv2.ellipse(image,(250,250),(100,50),30,0,180,(3,252,19),5)
#cv2.ellipse(image,(250,250),(100,50),30,0,180,(3,252,19),-1) 
points = np.array([[50,300],[150,200],[250,350],[200,350],[100,350]],np.int32)
points = points.reshape((-1,1,2))
cv2.fillPoly(image,[points],(123,3,252))
cv2.imshow('line',image)





cv2.waitKey(0)
