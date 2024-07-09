import cv2
import numpy as np

resim=cv2.imread("piksel2.jpg")

resim[50,30]=[255,255,255]

for i in range(0,100):
    for k in range(0,100):
        resim[i,k]=[255,255,255]
    



cv2.imshow("ist",resim)
cv2. waitKey(0)
cv2.destroyAllWindows()