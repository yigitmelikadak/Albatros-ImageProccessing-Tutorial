import cv2 as cv
import numpy as np

def contourdetection():
    img = cv.imread('Resources/Photos/cats.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    cv.imshow('cats', img)
    canny = cv.Canny(img, 125, 175)
    canny2 = cv.Canny(blur, 125, 175)
    cv.imshow('canny', canny)
    cv.imshow('canny2', canny2)
    contours, hierarchies = cv.findContours(canny2, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    # RETR_EXTERNAL -> only external contours
    # RETR_LIST -> all the contours
    # CHAIN_APPROX_SIMPLE -> simply merge neared contours
    print(f'{(len(contours))} contour/s found!')
    cv.waitKey(0)


def contouralternative():
    img = cv.imread('Resources/Photos/cats.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    cv.imshow('cats', img)

    blank = np.zeros(gray.shape, dtype="uint8")
    cv.imshow('blank', blank)

    # https://docs.opencv.org/5.0/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html
    ret, thresh = cv.threshold(blur, 125, 255, cv.THRESH_BINARY)
    cv.imshow('thresh', thresh)

    contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    print(f'{(len(contours))} contour/s found!')

    cv.drawContours(blank, contours, -1, (255, 255, 255), 1)
    cv.imshow('Contours', blank)

    cv.waitKey(0)