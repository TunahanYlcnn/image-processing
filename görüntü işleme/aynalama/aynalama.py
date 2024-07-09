import cv2
import numpy as np

resim=cv2.imread("resim1.webp")

aynalananresim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)
uzatma=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REPLICATE)
tekrar=cv2.copyMakeBorder(resim,300,300,300,300,cv2.BORDER_WRAP)
çerçeve=cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT,value=(0,0,255))



#cv2.imshow("çerçeve",çerçeve)
#cv2.imshow("tekrar",tekrar)
#cv2.imshow("uzatilanresim",uzatma)
#cv2.imshow("aynanilanresim",aynalananresim)

cv2.waitKey(0)
cv2.destroyAllWindows()