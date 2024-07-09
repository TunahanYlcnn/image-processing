import cv2


yuz=cv2.CascadeClassifier("front1.xml")
goz=cv2.CascadeClassifier("eye.xml")

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = yuz.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(200,0,0),3)
        frame2=frame[y:y+h,x:x+h]
        gray2=gray[y:y+h,x:x+h]

        gozler=goz.detectMultiScale(gray2)
    
        for x1,y1,w1,h1 in gozler:
            cv2.rectangle(frame2,(x1,y1),(x1+w1,y1+h1),(0,0,255),3)
       
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
      


cv2.imshow("1",frame)
cv2.destroyAllWindows
