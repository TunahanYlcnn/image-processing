import cv2 as cv
import numpy as np

image=cv.imread("gro.jpg")
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(gray,(3,3),0)


canny=cv.Canny(blur,50,150)

def autocanny(blur,sigma=0.50):
    median=np.median(blur)
    lower=int(max(0,(1.0-sigma)*median))
    upper=int(min(255,(1.0+sigma)*median))
    canny=cv.Canny(blur,lower,upper)
    
    return canny

    
wide=cv.Canny(blur,10,220)
tight=cv.Canny(blur,200,230)
auto=autocanny(blur)




cv.imshow("edges",np.hstack([wide,tight,auto]))

cv.waitKey(0)
cv.destroyAllWindows()