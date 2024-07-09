import cv2 
import numpy as np

resim=cv2.imread("278.JPG")
resimgri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

yukseklik,genislik,kanalsayisi=resim.shape
print("resim",yukseklik,genislik,kanalsayisi)


cv2.imshow("gri",resimgri)
cv2.waitKey(0)
cv2.destroyAllWindows()
