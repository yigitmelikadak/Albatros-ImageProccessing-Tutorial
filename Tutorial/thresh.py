import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#Simple Thresholding
threshold, thres = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('threshold', thres)

#Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive_thresh', adaptive_thresh)

cv.waitKey(0)