import cv2
import time
from gestures import hands, detect_gesture, draw_hands
from music_control import control_spotify, get_current_track_info
from ui import display_ui

# Cooldown timer for gestures
last_action_time = 0
cooldown = 2  # seconds

# Initial track info
current_track, current_artists, album_art = get_current_track_info()

# Start video feed
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    gesture = "No Hand"
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            draw_hands(frame, hand_landmarks)
            gesture = detect_gesture(hand_landmarks.landmark)

            current_time = time.time()
            if gesture not in ["No Action", "No Hand"] and (current_time - last_action_time > cooldown):
                control_spotify(gesture)
                current_track, current_artists, album_art = get_current_track_info()
                last_action_time = current_time

    # Update UI
    frame = display_ui(frame, gesture, current_track, current_artists, album_art)
    cv2.imshow('AI DJ - Gesture Control', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
