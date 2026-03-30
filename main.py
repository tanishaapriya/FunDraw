import cv2
from src.face_detection import detect_face
from src.hand_tracking import detect_hand
from src.gesture_control import get_index_finger, count_fingers
from src.drawing_utils import draw, set_color, clear_canvas
from src.color_palette import draw_palette, select_color

cap = cv2.VideoCapture(0)

# Gesture stability variables
prev_gesture = 0
gesture_counter = 0
stable_gesture = 0

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    faces = detect_face(frame)

    if len(faces) > 0:
        landmarks = detect_hand(frame)

        if landmarks:
            finger = get_index_finger(landmarks)
            fingers = count_fingers(landmarks)

            # 🔥 STABILITY LOGIC
            if fingers == prev_gesture:
                gesture_counter += 1
            else:
                gesture_counter = 0

            prev_gesture = fingers

            if gesture_counter > 5:
                stable_gesture = fingers

            if finger:
                x, y = finger

                # 🎨 Color selection
                selected = select_color(x, y)
                if selected:
                    set_color(selected)

                # ✌️ Gesture control
                if stable_gesture == 1:
                    draw(frame, x, y)

                elif stable_gesture == 2:
                    pass  # Pause

                elif stable_gesture == 3:
                    clear_canvas()

    draw_palette(frame)

    cv2.putText(frame, f"Gesture: {stable_gesture}", (10, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("FUNRAW - Air Drawing", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

    if key == ord('s'):
        cv2.imwrite("output/drawing.png", frame)
        print("Saved!")

cap.release()
cv2.destroyAllWindows()