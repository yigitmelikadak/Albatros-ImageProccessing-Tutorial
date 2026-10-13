import cv2 as cv
import numpy as np

#uint8 is related type to picture
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)


def paintimagecertaincolor():
    blank[0:100,20:30] = 255,0,0
    cv.imshow('blue',blank)


def drawarectangle():
    # draw a rectangle img, pt1(origin (left top)), pt2(width and height), color(b,g,r)
    # thickness = cv.FILLED for filling
    # blank.shape[0] and blank.shape[1] is used for scaling
    # blank.shape[0] height and blank.shape[1] is width it's quite tricky fr fr
    cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (255, 100, 0), thickness=cv.FILLED)
    cv.imshow('blank', blank)
    # if I named this same variable (blank), open one window(overwrite)


def drawacircle():
    # draw a circle
    # blank, center(middle-pivot), radius, color, thickness
    cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (255, 100, 0), thickness=cv.FILLED)
    cv.imshow('Circle', blank)


def drawaline():
    # draw a line
    # start point, end point, color, thickness
    cv.line(blank, (0, 0), (100, 200), (255, 255, 255), thickness=2)
    cv.imshow('line', blank)
    cv.waitKey(0)


def typeatext():
    # write a text
    # blank, string, origin(start point for text), font, font-size, color, thickness
    cv.putText(blank, 'Hello World', (250, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 3)
    cv.imshow("Text", blank)
    cv.waitKey(0)
