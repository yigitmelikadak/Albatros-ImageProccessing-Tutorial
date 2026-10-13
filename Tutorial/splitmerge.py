import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

b,g,r = cv.split(img)

blank = np.zeros(img.shape[:2], dtype="uint8")
blue = cv.merge((b,blank,blank))
green = cv.merge((blank,g,blank))
red = cv.merge((blank,blank,r))

#grayscale
cv.imshow('B', b)
cv.imshow('G', g)
cv.imshow('R', r)

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey(0)