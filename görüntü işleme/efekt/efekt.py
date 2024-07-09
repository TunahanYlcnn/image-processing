import cv2
import numpy as np

resim=cv2.imread("resim1.webp")
resim[120:200,200,250:0]=255
resim[120:200,200:250,1]=255
resim[120:200,200:250,2]=255
cv2.imshow("efekt",resim)



cv2.waitKey(0)
cv2.destroyAllWindows()
