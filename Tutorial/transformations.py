import cv2 as cv
import numpy as np

park = cv.imread('Resources/Photos/park.jpg')
cv.imshow('original', park)


def translationexample():
    def translate(img, x, y):
        transMat = np.float32([[1, 0, x], [0, 1, y]])
        dimensions = (img.shape[1], img.shape[0])
        return cv.warpAffine(img, transMat, dimensions)

    translated = translate(park, 50, -30)
    cv.imshow('translated', translated)
    cv.waitKey(0)


def rotationexample():
    def rotate(img, angle, rotPoint=None):
        (height, width) = img.shape[:2]

        if rotPoint == None:
            rotPoint = (width // 2, height // 2)

        rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width, height)
        return cv.warpAffine(img, rotMat, dimensions)

    rotated = rotate(park, 45)
    cv.imshow('rotated', rotated)
    cv.waitKey(0)


def flipping():
    # Flipping
    flip = cv.flip(park, 0)
    flip2 = cv.flip(park, 1)
    flip3 = cv.flip(park, -1)

    cv.imshow('flip', flip)  # upside down
    cv.imshow('flip2', flip2)  # horizontal
    cv.imshow('flip3', flip3)  # both
    cv.waitKey(0)