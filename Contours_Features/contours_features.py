import cv2 as cv 
import numpy as np

img_path = '../Images/sample-image3.png'
#  reading the images 
img = cv.imread(img_path)

denoised_img = cv.GaussianBlur(img, (3,3), 10)

edges_img = cv.Canny(denoised_img, 100,200)
dilate_img = cv.dilate(edges_img, (3,3), iterations=3)
contours, h = cv.findContours(dilate_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
for cnt  in contours:
    bbox = cv.boundingRect(cnt)
    # print(type(bbox))
    cv.rectangle(img, bbox, color=(0,0, 0), thickness=3)
    rect = cv.minAreaRect(cnt)
    # print(rect)
    box = cv.boxPoints(rect)
    
    box = np.int0(box)
    center, radius = cv.minEnclosingCircle(cnt)
    # pri))
    center = np.array(center).astype(int)
    cv.circle(img, center, int(radius), (0,255, 0), 2)
    print(center)
    cv.drawContours(img, [box], 0, (0,255, 0), 2)
    ellipse = cv.fitEllipse(cnt)
    img = cv.ellipse(img,ellipse,(255,0,255),2)
    [vx,vy,x,y] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0.01)
    print(vx, vy, x, y)
    rows,cols = img.shape[:2]
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)
    img = cv.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
    # cv.rectangle(img, box, color=(0, 255, 0),thickness=2 )
    cv.imshow('img', img)
    cv.waitKey(0)

cv.imshow('dilated_img', dilate_img)
# cv.imshow('img', img)
# cv.imshow('edges', edges_img)
cv.waitKey(0)
cv.destroyAllWindows()
