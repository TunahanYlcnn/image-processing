import cv2
import numpy as np

kalman = cv2.KalmanFilter(4, 2) 
kalman.transitionMatrix = np.array([[1, 0, 1, 0],
                                    [0, 1, 0, 1],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]], dtype=np.float32)

kalman.measurementMatrix = np.array([[1, 0, 0, 0],
                                     [0, 1, 0, 0]], dtype=np.float32)

kalman.processNoiseCov = np.eye(4, dtype=np.float32) * 0.01
kalman.measurementNoiseCov = np.eye(2, dtype=np.float32) * 0.03

kalman.statePre = np.array([[200], [150], [4], [3]], dtype=np.float32) # İlk durum vektörünü belirle

# Nesnenin başlangıç konumu ve hızı
object_pos = np.array([200, 150], np.float32)
velocity = np.array([4, 3], np.float32)

cv2.namedWindow("Kalman Tracking")

while True:
    frame = np.zeros((400, 400, 3), dtype=np.uint8)  
    object_pos += velocity # Gerçek pozisyonu güncelle

    # Duvara çarpınca yön değiştir
    if object_pos[0] <= 0 or object_pos[0] >= 400:
        velocity[0] *= -1
    if object_pos[1] <= 0 or object_pos[1] >= 400:
        velocity[1] *= -1
    
    measurement = object_pos + np.random.randn(2) # Ölçüm yap (biraz gürültü ekleyerek)
    kalman.correct(measurement.reshape(2, 1).astype(np.float32))
    prediction = kalman.predict() # Kalman filtresi ile tahmin yap
    cv2.circle(frame, (int(object_pos[0]), int(object_pos[1])), 10, (0, 255, 0), -1) # Gerçek konum (Yeşil)
    cv2.circle(frame, (int(prediction[0]), int(prediction[1])), 10, (0, 0, 255), 2) # Kalman filtresi tahmini (Kırmızı)

    cv2.imshow("Kalman Tracking", frame)
    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()