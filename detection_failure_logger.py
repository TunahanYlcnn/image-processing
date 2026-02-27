import cv2
from ultralytics import YOLO
import os

model = YOLO("C:/Users/tunahan/Desktop/vs/bestv8.pt", verbose = False)
cap = cv2.VideoCapture("C:/Users/tunahan/Desktop/vs/vid10.mp4") 


os.makedirs("missed_frames", exist_ok=True)

frame_id = 39094 
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose = False)
    boxes = results[0].boxes

    if len(boxes) == 0:
        filename = os.path.join("missed_frames", f"missed_{frame_id:05d}.jpg")
        cv2.imwrite(filename, frame)

    frame_id+=1