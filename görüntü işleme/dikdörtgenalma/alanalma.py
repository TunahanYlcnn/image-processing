import cv2
import numpy as np
 
resim=cv2.imread("hababam.jpg")
cv2.rectangle(resim,(200,10),(250,40),[0,0,255],1)

cv2.imshow("hababam",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()