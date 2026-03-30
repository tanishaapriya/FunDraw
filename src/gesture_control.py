def count_fingers(landmarks):
    if not landmarks:
        return 0

    fingers = []

    tips = [4, 8, 12, 16, 20]

    if landmarks[4][1] > landmarks[3][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    for tip in tips[1:]:
        if landmarks[tip][2] < landmarks[tip - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers.count(1)


def get_index_finger(landmarks):
    for id, x, y in landmarks:
        if id == 8:
            return x, y
    return None
