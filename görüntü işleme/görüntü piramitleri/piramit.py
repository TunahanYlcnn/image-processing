import cv2
import numpy as np

resim=cv2.imread("477.JPG")
ikikat=cv2.pyrUp(resim)
kucuk=cv2.pyrDown(resim)

print("orjinal=",resim.shape)
print("ikikat=",ikikat.shape)
print("küçük",kucuk.shape)

cv2.imshow("resim",resim)
cv2.imshow("büyük",ikikat)
cv2.imshow("kucuk",kucuk)

cv2.waitKey(0)
cv2.destroyAllWindows()