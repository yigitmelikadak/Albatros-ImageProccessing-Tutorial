import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0, cv.CAP_DSHOW)

kernel = np.ones((5, 5), np.uint8)

width = int(capture.get(3))
height = int(capture.get(4))

masked = np.zeros((height, width, 3), np.uint8)

p_width = width // 3
p_height = height // 3

lower = np.array([0, 168, 93])
upper = np.array([10, 255, 240])

def draw_lines():
    # üşendim böyle yaptım.
    p10 = (p_width, 0)
    p11 = (p_width, height)

    p20 = (p_width * 2, 0)
    p21 = (p_width * 2, height)

    p30 = (0, p_height)
    p31 = (width, p_height)

    p40 = (0, p_height * 2)
    p41 = (width, p_height * 2)

    line_color = (0, 255, 0)
    thickness = 2

    cv.line(masked, p10, p11, line_color, thickness=thickness)
    cv.line(masked, p20, p21, line_color, thickness=thickness)
    cv.line(masked, p30, p31, line_color, thickness=thickness)
    cv.line(masked, p40, p41, line_color, thickness=thickness)

draw_lines()

while True:
    square = []
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)

    smoothed = cv.medianBlur(frame, 5)
    into_hsv = cv.cvtColor(smoothed, cv.COLOR_BGR2HSV)

    mask = cv.inRange(into_hsv, lower, upper)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations=1)
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel, iterations=2)

    _, thresh_mask = cv.threshold(mask, 127, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(thresh_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv.contourArea(contour) >= 926:
            square.append(contour)
            print(f"{len(square)} bulundu.")

    frame = cv.bitwise_or(frame, masked)
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break