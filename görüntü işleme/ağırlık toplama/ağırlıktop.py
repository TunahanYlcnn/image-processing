import cv2
import numpy as np

resim=cv2.imread("216.JPG")
resim1=cv2.imread("212.JPG")

print(resim[50,200])
print(resim1[200,250])


cv2.waitKey(0)
cv2.destroyAllWindows()


print("toplamları=",resim[50,200]+resim1[20,250])