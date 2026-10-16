import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0, cv.CAP_DSHOW)

kernel = np.ones((5, 5), np.uint8)

width = int(capture.get(3))
height = int(capture.get(4))

masked = np.zeros((height, width, 3), np.uint8)

p_width = width // 3
p_height = height // 3

red_lower = np.array([170, 85, 0])
red_upper = np.array([179, 200, 255])

green_lower = np.array([35, 40, 40])
green_upper = np.array([93, 200, 255])

def whichsquare(x,y):
    if y > 0 and y <= p_height:
       height = "A"
    elif y > p_height and y <= p_height * 2:
        height = "B"
    else:
        height = "C"
    if x > 0 and x <= p_width:
        width = "1"
    elif x > p_width and x <= p_width * 2:
        width = "2"
    else:
        width = "3"
    return height + width

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

    red_mask = cv.inRange(into_hsv, red_lower, red_upper)
    red_mask = cv.morphologyEx(red_mask, cv.MORPH_OPEN, kernel, iterations=1)
    red_mask = cv.morphologyEx(red_mask, cv.MORPH_CLOSE, kernel, iterations=2)

    green_mask = cv.inRange(into_hsv, green_lower, green_upper)
    green_mask = cv.morphologyEx(green_mask, cv.MORPH_OPEN, kernel, iterations=1)
    green_mask = cv.morphologyEx(green_mask, cv.MORPH_CLOSE, kernel, iterations=2)

    _, red_thresh_mask = cv.threshold(red_mask, 200, 255, cv.THRESH_BINARY)
    _, green_thresh_mask = cv.threshold(green_mask, 200, 255, cv.THRESH_BINARY)
    red_contours, _ = cv.findContours(red_thresh_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    green_contours, _ = cv.findContours(green_thresh_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for contour in red_contours:
        if cv.contourArea(contour) >= 1300:
            square.append(contour)
            cv.drawContours(frame, [contour], -1, (0, 0, 255), 2)
            x, y, w, h = cv.boundingRect(contour)
            cX = x + (w // 2)
            cY = y + (h // 2)
            cv.putText(frame, f"Bulundu: {whichsquare(cX,cY)}", (cX - 20, cY), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    for contour in green_contours:
        if cv.contourArea(contour) >= 1300:
            square.append(contour)
            cv.drawContours(frame, [contour], -1, (0, 255, 0), 2)
            x, y, w, h = cv.boundingRect(contour)
            cX = x + (w // 2)
            cY = y + (h // 2)
            cv.putText(frame, f"Bulundu: {whichsquare(cX,cY)}", (cX - 20, cY), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    frame = cv.bitwise_or(frame, masked)
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break