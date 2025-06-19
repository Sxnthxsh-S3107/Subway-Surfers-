import cv2
import mediapipe as mp
import pyautogui
import time

# MediaPipe setup (real-time optimized)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.6,
    static_image_mode=False
)

# Camera setup
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

# Finger tip landmarks (ignoring thumb for stability)
TIP_IDS = [8, 12, 16, 20]

def count_fingers(hand_landmarks):
    count = 0
    for tip_id, pip_id in zip(TIP_IDS, [6, 10, 14, 18]):
        if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[pip_id].y:
            count += 1
    return count

# Cooldown mechanism
last_action = None
last_time = 0
cooldown = 0.3  # fast reaction

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            finger_count = count_fingers(hand_landmarks)
            current_time = time.time()

            action = None
            if finger_count == 1:
                action = "up"     # Jump
            elif finger_count == 2:
                action = "down"   # Slide
            elif finger_count == 3:
                action = "left"   # Move left
            elif finger_count == 4:
                action = "right"  # Move right

            if action and (action != last_action or current_time - last_time > cooldown):
                pyautogui.press(action)
                last_action = action
                last_time = current_time
                cv2.putText(frame, f"{action.upper()}", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)

    # Display
    cv2.imshow("Subway Gesture Controller", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
