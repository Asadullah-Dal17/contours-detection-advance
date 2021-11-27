import cv2 as cv 
import numpy as np


img = cv.imread('Images/sample-image3.png')

# denoiseing image 
cv.imshow('img', img)
cv.waitKey(0)
denosied_img = cv.GaussianBlur(img, (3,3), 0)

# finding Edges 
edges_img = cv.Canny(denosied_img, 100, 130)
cv.imshow('edges', edges_img)
cv.imshow('img', img)
cv.waitKey(0)

