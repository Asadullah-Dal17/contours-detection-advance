import cv2 as cv 
import numpy as np

img_path = '../Images/sample.jpg'
#  reading the images 
img = cv.imread(img_path)

denoised_img = cv.GaussianBlur(img, (3,3), 10)

edges_img = cv.Canny(denoised_img, 100,200)
dilate_img = cv.dilate(edges_img, (3,3), iterations=3)

cv.imshow('dilated_img', dilate_img)
# cv.imshow('img', img)
# cv.imshow('edges', edges_img)
cv.waitKey(0)
cv.destroyAllWindows()
