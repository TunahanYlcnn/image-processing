import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

# El takip modelini başlat
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        # Elleri tespit et
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Parmağın uç noktasının pozisyonlarına bakarak elin durumunu belirleme
                finger_tips = [4, 8, 12, 16, 20]  # İlgili parmak uçlarının indexleri
                finger_states = []

                for i in range(5):
                    # Parmağın aşağıya doğru kıvrılıp kıvrılmadığını kontrol et
                    if hand_landmarks.landmark[finger_tips[i]].y < hand_landmarks.landmark[finger_tips[i] - 2].y:
                        finger_states.append(1)  # Parmağın açık olduğunu belirtir
                    else:
                        finger_states.append(0)  # Parmağın kapalı olduğunu belirtir

                # Parmak sayısını hesapla
                finger_count = sum(finger_states)
                print(f"Elin Pozisyonu: {finger_count}")

        cv2.imshow("El Takibi", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
