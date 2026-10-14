import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def part_one():
    img = cv.imread('Resources/Photos/cats.jpg')
    cv.imshow('cats', img)

    blank = np.zeros(img.shape[:2], dtype='uint8')

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)

    circle = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
    mask = cv.bitwise_and(gray, gray, mask=circle)

    # grayscale histogram
    gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

    plt.figure()
    plt.title('Gray Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.plot(gray_hist)
    plt.xlim([0, 256])
    plt.show()
    cv.waitKey(0)


def part_two():
    img = cv.imread('Resources/Photos/cats.jpg')
    cv.imshow('cats', img)

    blank = np.zeros(img.shape[:2], dtype='uint8')

    circle = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)

    mask = cv.bitwise_and(img, img, mask=circle)
    cv.imshow('mask', mask)

    plt.figure()
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')

    colors = ('b', 'g', 'r')
    for i, col in enumerate(colors):
        hist = cv.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.show()

    cv.waitKey(0)
