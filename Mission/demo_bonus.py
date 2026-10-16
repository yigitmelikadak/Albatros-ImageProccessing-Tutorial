import cv2 as cv
import asyncio
import numpy as np

capture = cv.VideoCapture(0)

width = int(capture.get(3))
height = int(capture.get(4))

masked = np.zeros((height, width, 3), np.uint8)

p_width = width // 3
p_height = height // 3







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

async def camera_interface():
    await asyncio.sleep(.1)
    draw_lines()
    while True:
        properly, frame = capture.read()
        frame = cv.bitwise_or(frame, masked)
        cv.imshow('Video', frame)
        await asyncio.sleep(0.001)
        if cv.waitKey(20) & 0xFF == ord('q'):
            break


async def detect_object():
    print("a")
    await asyncio.sleep(.1)
    while True:
        #https://www.geeksforgeeks.org/python/real-time-object-color-detection-using-opencv/
        properly, frame = capture.read()
        into_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        into_hsv_blurred = cv.GaussianBlur(into_hsv, (5, 5), 0)
        cv.imshow('Video2', into_hsv_blurred)
        await asyncio.sleep(0.001)
        await asyncio.gather(detect_object_red(into_hsv, properly, frame),
                             detect_object_orange(into_hsv, properly, frame),
                             detect_object_yellow(into_hsv, properly, frame),
                             detect_object_green(into_hsv, properly, frame),
                             detect_object_blue(into_hsv, properly, frame),
                             detect_object_cyan(into_hsv, properly, frame),
                             detect_object_purple(into_hsv, properly, frame),
                             )
        if cv.waitKey(20) & 0xFF == ord('q'):
            break

L_red1 = np.array([0, 40, 40])
U_red1 = np.array([10, 255, 255])
L_red2 = np.array([170, 40, 40])
U_red2 = np.array([179, 255, 255])
# Kırmızı (Red)
async def detect_object_red(into_hsv, properly, frame):
    r_mask = cv.bitwise_or(cv.inRange(into_hsv, L_red1, U_red1), cv.inRange(into_hsv, L_red2, U_red2))
    red = cv.bitwise_and(frame, frame, mask=r_mask)
    cv.imshow('red', red)

L_orange = np.array([11, 40, 40])
U_orange = np.array([25, 255, 255])
# Turuncu (Orange)
async def detect_object_orange(into_hsv, properly, frame):
    mask = cv.inRange(into_hsv, L_orange, U_orange)
    orange = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('orange', orange)

L_yellow = np.array([26, 40, 40])
U_yellow = np.array([34, 255, 255])
# Sarı (Yellow)
async def detect_object_yellow(into_hsv, properly, frame):
        mask = cv.inRange(into_hsv, L_yellow, U_yellow)
        yellow = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow('yellow', yellow)

L_green = np.array([35, 40, 40])
U_green = np.array([85, 255, 255])
# Yeşil (Green)
async def detect_object_green(into_hsv, properly, frame):
        mask = cv.inRange(into_hsv, L_green, U_green)
        green = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow('green', green)

L_cyan = np.array([86, 40, 40])
U_cyan = np.array([99, 255, 255])
# Cam Göbeği (Cyan)
async def detect_object_cyan(into_hsv, properly, frame):
        mask = cv.inRange(into_hsv, L_cyan, U_cyan)
        cyan = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow('cyan', cyan)

L_blue = np.array([100, 40, 40])
U_blue = np.array([130, 255, 255])
# Mavi (Blue)
async def detect_object_blue(into_hsv, properly, frame):
        mask = cv.inRange(into_hsv, L_blue, U_blue)
        blue = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow('blue', blue)

L_purple = np.array([131, 40, 40])
U_purple = np.array([169, 255, 255])
# Mor (Purple)
async def detect_object_purple(into_hsv, properly, frame):
    mask = cv.inRange(into_hsv, L_purple, U_purple)
    purple = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('purple', purple)

async def main():
    await asyncio.gather(camera_interface(), detect_object())

asyncio.run(main())