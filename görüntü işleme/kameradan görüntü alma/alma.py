import cv2 as cv
import numpy as np

kamera=cv.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()
    cv.imshow("goruntu",goruntu)
    if cv.waitKey(30) & 0xFF==('q'):
        break    

kamera.release()

cv.destroyAllWindow()
    
    
    
    