import cv2 as cv
import numpy as np

image=cv.imread("ress.png")
kernel=np.ones((5,5),np.uint8)

eros=cv.erode(image,kernel,iterations=1)
day=cv.dilate(image,kernel,iterations=1)
day2=cv.dilate(eros,kernel,iterations=1)
grande=cv.morphologyEx(image,cv.MORPH_GRADIENT,kernel)

open=cv.morphologyEx(image,cv.MORPH_OPEN,kernel)
close=cv.morphologyEx(image,cv.MORPH_CLOSE,kernel)

top=cv.morphologyEx(image,cv.MORPH_TOPHAT,kernel)
black=cv.morphologyEx(image,cv.MORPH_BLACKHAT,kernel)


cv.imshow("balck",black)
cv.imshow("top",top)
cv.imshow("close",close)
cv.imshow("open",open)
cv.imshow("day",day)
cv.imshow("res",image)
cv.imshow("ero",eros)
cv.imshow("day2",day2)
cv.imshow("grade",grande)

cv.waitKey(0)
cv.destroyAllWindows()