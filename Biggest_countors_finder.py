import cv2 as cv 
import numpy as np
def findBiggestContour(img, contours):
    if len(contours):
        c = max(contours, key = cv.contourArea)
        print(c)
        x,y,w,h = cv.boundingRect(c)
        # draw the biggest contour (c) in green
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        return c
    else:
        return None
    
img = cv.imread('./Images/sample-image2.png')
blur_image = cv.GaussianBlur(img, (3,3),0)
edges_img = cv.Canny(blur_image, 100, 150)
cv.imshow('edges', edges_img)
contours, h = cv.findContours(edges_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
max_area =0
area_list =[]

big_cont =findBiggestContour(img, contours)
print(big_cont)

# for index, c in enumerate(contours):
#     area = cv.contourArea(c)
#     print(area)
#     # getting centroid points of contour
#     M = cv.moments(c)
#     # print(center_point)
#     cx = int(M['m10']/M['m00'])
#     cy = int(M['m01']/M['m00'])
#     # Putting text, as Area of Found contours, 
#     # cv.circle(img,(cx, cy), 2, 255, -1)
#     area_list.append([area])
#     data_list.append([c,])


    # if area >max_area:
    #     max_area = area
    #     big_contours= c
    # if c is None:
    #     cv.putText(img, f'{area} Biggest', (cx, cy), cv.FONT_HERSHEY_PLAIN, 1, (255,0,244), 2, cv.LINE_AA)
print(area_list, 'biggest')
# cv.drawContours(img, contours, -1, 255, 2)
# cv.drawContours(img, big_contours,-1, (0,255,0), 7)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()