import cv2 as cv 
import numpy as np

def findBiggestContour(img, contours):
    # looping through All The contours 
    for cnt  in contours:
        area = cv.contourArea(cnt)
        M = cv.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv.putText(img, f'{area} Area', (cx-18, cy-5), cv.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,0), 1)
    # finding biggest contour 
    c = max(contours, key = cv.contourArea)    
    area =cv.contourArea(c)
    x,y,w,h = cv.boundingRect(c)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    return c

img = cv.imread('../Images/sample-image3.png')

blur_image = cv.GaussianBlur(img, (3,3),0)
edges_img = cv.Canny(blur_image, 100, 150)
cv.imshow('edges', edges_img)
contours, h = cv.findContours(edges_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, 255, 2)
big_cont =findBiggestContour(img, contours)

cv.imshow('img', img)
cv.imwrite('/results/biggest_contours_out.png', img)
cv.waitKey(0)
cv.destroyAllWindows()