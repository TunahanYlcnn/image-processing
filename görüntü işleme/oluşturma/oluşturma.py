import cv2 as cv
import numpy as np

resim=np.zeros((300,300,3),dtype="uint8")

cv.line(resim,(0,0),(100,100),(0,0,255),3)
cv.circle(resim,(100,150),25,(0,255,0),2)

cv.putText(resim,"tunahan",(100,200),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),8)

cv.imshow("deneme",resim)
cv.waitKey(0)
cv.destroyAllWindows()







