import cv2

points = []
current_color = (255, 0, 0)

def set_color(color):
    global current_color
    current_color = color

def draw(frame, x, y):
    global points

    points.append((x, y))

    # Smooth drawing
    for i in range(1, len(points)):
        cv2.line(frame, points[i-1], points[i], current_color, 5)

def clear_canvas():
    global points
    points = []
    