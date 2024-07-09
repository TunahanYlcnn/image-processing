import cv2 as cv
import numpy as np

image=cv.imread("ress.png")

kernel=np.ones((5,5),np.uint8)

eros=cv.erode(image,kernel,iterations=1)
day=cv.dilate(eros,kernel,iterations=1)


cv.imshow("day",day)
cv.imshow("res",image)
cv.imshow("ero",eros)

cv.waitKey(0)
cv.destroyAllWindows()










