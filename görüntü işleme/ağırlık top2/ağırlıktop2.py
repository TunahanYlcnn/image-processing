import cv2 
import numpy as np

resim=cv2.imread("158.JPG")
resim1=cv2.imread("160.JPG")

toplam=cv2.add(resim,resim1)
agirliktoplam=cv2.addWeighted(resim,0.9,resim1,0.1,0 )

cv2.imshow("agirlik",agirliktoplam)
cv2.imshow("toplanmiş resimler",toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()