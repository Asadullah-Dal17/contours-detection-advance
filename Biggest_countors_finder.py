import cv2 as cv 
import numpy as np

def findBiggestContour(img, contours):
    # looping through All The contours 
    for cnt  in contours:
        area = cv.contourArea(cnt)
        M = cv.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv.putText(img, f'{area} Area', (cx, cy), cv.FONT_HERSHEY_PLAIN, 1, (255,0,244), 2, cv.LINE_AA)
    # finding biggest contour 
    c = max(contours, key = cv.contourArea)    
    area =cv.contourArea(c)
    x,y,w,h = cv.boundingRect(c)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    return c

img = cv.imread('./Images/sample-image.png')
blur_image = cv.GaussianBlur(img, (3,3),0)
edges_img = cv.Canny(blur_image, 100, 150)
cv.imshow('edges', edges_img)
contours, h = cv.findContours(edges_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, 255, 2)
big_cont =findBiggestContour(img, contours)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()