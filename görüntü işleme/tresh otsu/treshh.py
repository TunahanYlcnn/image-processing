import cv2 as cv


image2=cv.imread("parnak.png",0)


#simple thresh
ret,thresh1=cv.threshold(image2,160,255,cv.THRESH_BINARY)

#adaptive treshhold
thresh2=cv.adaptiveThreshold(image2,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                            cv.THRESH_BINARY,11,2)

thresh3=cv.adaptiveThreshold(image2,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
                            cv.THRESH_BINARY,11,2)

#otsu tresh
ret4,tresh4=cv.threshold(image2,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)




cv.imshow("renk",image2)
cv.imshow("thresh1",thresh1)
cv.imshow("thresh2",thresh2)
cv.imshow("thresh3",thresh3)
cv.imshow("tresh4",tresh4)

cv.waitKey(0)
cv.destroyAllWindows()