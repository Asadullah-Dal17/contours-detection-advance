import cv2 as cv 
import numpy as np
img = cv.imread('./sample-image.png')
blur_image = cv.GaussianBlur(img, (3,3),0)
edges_img = cv.Canny(blur_image, 100, 150)
cv.imshow('edges', edges_img)
contours, h = cv.findContours(edges_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
max_area =0
for c in contours:
    area = cv.contourArea(c)
    print(area)
    
    if area >max_area:
        max_area = area
        big_contours= c
cv.drawContours(img, contours, -1, 255, 2)
cv.drawContours(img, big_contours,-1, (0,255,0), 7)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()