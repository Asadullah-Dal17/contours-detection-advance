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
    perimeter = cv.arcLength(c, True)
    # print(perimeter)
    epsilon = 0.05*cv.arcLength(c,True)
    approx = cv.approxPolyDP(c,epsilon,True)
    print(f'appx: {approx}, perimeter: {perimeter}')
    # print(area)
    M = cv.moments(c)
    # print(center_point)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv.putText(img, f'{area} A, {len(approx)} APX', (cx, cy), cv.FONT_HERSHEY_PLAIN, 0.7, (0,255,244), 1, cv.LINE_AA)
    # # cv.circle(img,(cx, cy), 2, 255, -1)


    
cv.drawContours(img, contours, -1, 255, 2)
# cv.drawContours(img, big_contours,-1, (0,255,0), 7)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()