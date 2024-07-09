import cv2

img=cv2.imread("1.jpg")
yuz = cv2.CascadeClassifier("front1.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces =yuz.detectMultiScale(gray, 1.3, 4)

for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(200,0,0),2)



cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()