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

                # Parmağın uç noktalarını tanımla (yani, 4, 8, 12, 16, 20)
                finger_tips = [4, 8, 12, 16, 20]
                finger_states = []

                # Baş parmak için özel bir durum ekleyelim
                # Baş parmak: index 4
                if hand_landmarks.landmark[4].y < hand_landmarks.landmark[3].y and hand_landmarks.landmark[4].y < hand_landmarks.landmark[2].y:
                    finger_states.append(1)  # Baş parmak açık
                else:
                    finger_states.append(0)  # Baş parmak kapalı

                # Diğer parmaklar için açık mı kapalı mı olduğunu kontrol et
                for i in range(1, 5):
                    if hand_landmarks.landmark[finger_tips[i]].y < hand_landmarks.landmark[finger_tips[i] - 2].y:
                        finger_states.append(1)  # Parmağın açık olduğunu belirtir
                    else:
                        finger_states.append(0)  # Parmağın kapalı olduğunu belirtir

                # Parmak sayısını hesapla
                finger_count = sum(finger_states)
                landmarks_count = len(hand_landmarks.landmark)

               
                cv2.putText(frame, f"Landmarks Sayisi: {landmarks_count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(frame, f"Sayiniz: {finger_count}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

        cv2.imshow("El Takibi", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
