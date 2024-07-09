import cv2
import numpy as np

kurt=cv2.imread("kurt.jpg")

print("resmin belirlenen yerdeki rgb değeri=",kurt[(30,80)])
print("resimin boyutu=",kurt.size)
print("resmin veri tipi=",kurt.dtype)
print("resmin özellikleri=",kurt.shape)


cv2.imshow("kurt resmi",kurt)

cv2.waitKey(0)
cv2.destroyAllWindows()