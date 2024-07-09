import numpy as np
import cv2

resim=cv2.imread("resim1.webp")

cv2.imshow("iha tasarim",resim)

print(resim.size)
print(resim.dtype)
print(resim.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
