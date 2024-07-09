import cv2 as cv

image=cv.imread("filt.jpg")
meanfilter=cv.blur(image,(3,3))
meanfilter2=cv.blur(image,(3,3))

medianfilter=cv.medianBlur(image,3)
medianfilter2=cv.medianBlur(image,5)
medianfilter3=cv.medianBlur(image,7)

gauss=cv.GaussianBlur(image,(3,3),0)
gauss2=cv.GaussianBlur(image,(5,5),0)
gauss3=cv.GaussianBlur(image,(7,7),0)

cv.imshow("orjinasl",image)
cv.imshow("meanfilter",meanfilter)
cv.imshow("meanfilter2",meanfilter2)

cv.imshow("medianfilter",medianfilter)
cv.imshow("medianfilter2",medianfilter2)
cv.imshow("medianfilter3",medianfilter3)

cv.imshow("gauss",gauss)
cv.imshow("gauss2",gauss2)
cv.imshow("gauss3",gauss3)

cv.waitKey(0)
cv.destroyAllWindows()