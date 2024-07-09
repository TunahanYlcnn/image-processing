import cv2

net=cv2.dnn.readNet("dnn_model/yolov4-tiny.weights","dnn_model/yolov4-tiny.cfg")
model=cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320,320),scale=1/255)

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    
    (class_ids,score,bboxes)=model.detect(frame,confThreshold=0.3,nmsThreshold=4)
    for class_ids,score,bbox in zip(class_ids,score,bboxes):
        (x,y,w,h)=bbox
        cv2.rectangle(frame,(x,y),(x+w,y+h),(200,0,50),2)
    
    
    cv2.imshow("frame",frame)
    key=cv2.waitKey(1)
    if key ==27:
        break

cap.release()
cv2.destroyAllWindows()
        
    
    
    
    
    
    
    
    
    
