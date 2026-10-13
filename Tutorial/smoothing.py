import cv2 as cv
from numpy.ma.extras import average

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

#Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average', average)

#Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gauss', gauss)

#Median Blur
median = cv.medianBlur(img,7) #it's good for reduce noises
cv.imshow('Median', median)

#Bilateral --> The best, and the slowest one
bilateral = cv.bilateralFilter(img, 5, 15,15)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)