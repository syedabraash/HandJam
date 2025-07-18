import cv2

def display_ui(frame, gesture, track_name, artists, album_art):
    # Show album art
    if track_name and album_art is not None:
        album_art_resized = cv2.resize(album_art, (100, 100))
        frame[10:110, 10:110] = album_art_resized
        cv2.putText(frame, f'{track_name} - {artists}', (120, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)

    # Show gesture text
    cv2.putText(frame, f'Gesture: {gesture}', (10, frame.shape[0] - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

    return frame
