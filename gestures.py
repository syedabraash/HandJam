import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)

def detect_gesture(landmarks):
    if not landmarks:
        return "No Hand"

    thumb_tip = landmarks[4].y
    index_tip = landmarks[8].y
    middle_tip = landmarks[12].y
    ring_tip = landmarks[16].y
    pinky_tip = landmarks[20].y
    index_mcp = landmarks[5].y
    wrist = landmarks[0].y

    if all(tip < index_mcp for tip in [index_tip, middle_tip, ring_tip, pinky_tip]):  
        return "Play/Pause"
    elif index_tip < index_mcp and all(tip > index_mcp for tip in [middle_tip, ring_tip, pinky_tip]):
        return "Next Track"
    elif thumb_tip < wrist:
        return "Volume Up"
    elif thumb_tip > wrist:
        return "Volume Down"
    else:
        return "No Action"

def draw_hands(frame, hand_landmarks):
    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
