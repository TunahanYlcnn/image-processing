import cv2 as cv
import numpy as np

kamera=cv.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()
    
    cv.rectangle(goruntu,(100,100),(200,200),(0,0,255),2)
    cv.line(goruntu,(50,50),(300,300),(0,255,0),3)
    cv.circle(goruntu,(150,150),50,(255,0,0),3)
    cv.putText(goruntu,"tunahan",(220,220),cv.FONT_HERSHEY_DUPLEX,2,(0,0,255),1)
    
    cv.imshow("goruntu",goruntu)
    if cv.waitKey(25) & 0xFF==('q'):
        break
    

kamera.release

cv.destroyAllWindows()





