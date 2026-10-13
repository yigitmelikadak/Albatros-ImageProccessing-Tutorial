import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cat.jpg')
#cv.imshow('img', img)

blank = np.zeros(img.shape[:2],dtype='uint8')
#cv.imshow('blank', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100,255,-1)
#cv.imshow('mask', mask)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255,-1)
weirdmask = cv.bitwise_or(mask, rectangle)
masked = cv.bitwise_and(img, img, mask=weirdmask)
cv.imshow('masked', masked)

cv.waitKey(0)