import cv2

input_path = "VİDEO.mp4"
output_path = "KAYIT_VİDEO_İSMİ.mp4"

cap = cv2.VideoCapture(input_path)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    x_center = width // 2
    cv2.line(frame, (x_center, 0), (x_center, height), (0, 0, 0), thickness=3)
    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()
