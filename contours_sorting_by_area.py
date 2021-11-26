import cv2 as cv 
import numpy as np
def areaFinder(contours):
    areas = []
    for c in contours:
        a =cv.contourArea(c)
        areas.append(a)
    return areas
def sortedContoursByArea(img, larger_to_smaller=True):
    edges_img = cv.Canny(img, 100, 150)
    contours , h = cv.findContours(edges_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)   
    sorted_contours = sorted(contours, key=cv.contourArea, reverse=larger_to_smaller)
    return sorted_contours
img = cv.imread('./Images/sample-image.png')
sorted_contours = sortedContoursByArea(img, larger_to_smaller=True)
# print(areaFinder(contours))
print(areaFinder(sorted_contours))
for c in sorted_contours:
    cv.drawContours(img, c,  -1, 244, 3)
    cv.imshow('img', img)
    cv.waitKey(0)
cv.destroyAllWindows()