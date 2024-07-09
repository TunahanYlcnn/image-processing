import cv2
import numpy as np

resim=cv2.imread("resim1.webp")

kesit=resim[150:200,150:200]

resim[0:50,0:50]=kesit
kesit[:,:,0]=255
resim[60:100,70:100]=(25,150,80)

cv2.imshow("kesit",kesit)
cv2.imshow("kesitalma",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()