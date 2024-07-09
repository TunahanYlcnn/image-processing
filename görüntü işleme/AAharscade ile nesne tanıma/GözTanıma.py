import cv2

img=cv2.imread("1.jpg")
yuz=cv2.CascadeClassifier("front1.xml")
goz=cv2.CascadeClassifier("eye.xml")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=yuz.detectMultiScale(gri,1.3,4)

for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(200,0,0),3)
    
    img2=img[y:y+h,x:x+h]
    gri2=gri[y:y+h,x:x+h]

    gozler=goz.detectMultiScale(gri2)
    
    for x1,y1,w1,h1 in gozler:
        cv2.rectangle(img2,(x1,y1),(x1+w1,y1+h1),(0,0,255),3)


cv2.imshow("1",img)
cv2.waitKey(0)
cv2.destroyAllWindows



