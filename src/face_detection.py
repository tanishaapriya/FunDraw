import cv2
import os

# Absolute path fix
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))
model_path = os.path.join(project_root, "models", "haarcascade_frontalface_default.xml")

print("MODEL PATH:", model_path)  # DEBUG

face_cascade = cv2.CascadeClassifier(model_path)

def detect_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces
