import cv2 as cv
import matplotlib.pyplot as plt

def convertformat():
    img = cv.imread('Resources/Photos/park.jpg')
    cv.imshow('Park', img)
    # BGR to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)

    # https://www.geeksforgeeks.org/computer-graphics/hsv-color-model-in-computer-graphics/
    # https://stackoverflow.com/questions/17063042/why-do-we-convert-from-rgb-to-hsv
    # BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow('hsv', hsv)

    # BGR to L*A*B
    lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    cv.imshow('lab', lab)
    cv.waitKey(0)


def exampleforconversion():
    img = cv.imread('Resources/Photos/park.jpg')
    cv.imshow('Park', img)
    img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.imshow(img2)
    plt.show()

img = cv.imread('Resources/Photos/park.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#for Grayscale2HSV -> grayscale2BGR then BGR2HSV
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV ---> BGR', hsv_bgr)
cv.waitKey(0)
