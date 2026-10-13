import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('cat', img)


def convertgray():
    #converting to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray2 = cv.imread('Resources/Photos/cat.jpg', cv.IMREAD_GRAYSCALE)  # alternative
    cv.imshow('gray', gray)


def addblur():
    # blur
    # ksize(width,height) and values must be odd.
    blur = cv.GaussianBlur(img, (1, 21), cv.BORDER_DEFAULT)
    cv.imshow('blur', blur)
    cv.waitKey(0)


def edgecascadeanddilate():
    # edge cascade
    # img threshold1, threshold2
    # https://opencv.org/edge-detection-using-opencv/
    # add gaussian blur to the image before using canny is recomended.
    canny = cv.Canny(img, 100, 110)
    cv.imshow('canny', canny)
    # dilating the image
    dilated = cv.dilate(canny, (7, 7), iterations=3)
    cv.imshow('dilated', dilated)
    cv.waitKey(0)
    eroded = cv.erode(dilated, (7, 7), iterations=3)
    cv.imshow('eroded', eroded)


def resize():
    # resize
    # https://iq.opengenus.org/different-interpolation-methods-in-opencv/
    resized = cv.resize(img, (200, 200), interpolation=cv.INTER_AREA)  # better image decimation
    resized2 = cv.resize(img, (200, 200), interpolation=cv.INTER_LINEAR)  # default
    resized3 = cv.resize(img, (200, 200), interpolation=cv.INTER_CUBIC)  # 4x4

    cv.imshow('resized', resized)
    cv.imshow('resized2', resized2)
    cv.imshow('resized3', resized3)

#cropping
#y start y end, x start, x end
#https://opencv.org/cropping-an-image-using-opencv/
cropped =  img [200:600,0:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)