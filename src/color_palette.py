import cv2

colors = [
    ((255, 0, 0), (50, 50)),
    ((0, 255, 0), (110, 50)),
    ((0, 0, 255), (170, 50)),
    ((255, 255, 0), (230, 50)),
    ((255, 0, 255), (290, 50)),
    ((0, 255, 255), (350, 50)),
    ((0, 0, 0), (410, 50)),  # Eraser
]

def draw_palette(frame):
    for color, pos in colors:
        cv2.circle(frame, pos, 20, color, -1)

def select_color(x, y):
    for color, (cx, cy) in colors:
        if abs(x - cx) < 20 and abs(y - cy) < 20:
            return color
    return None
