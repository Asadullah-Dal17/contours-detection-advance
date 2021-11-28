import cv2 as cv 
import numpy as np

img_path = '../Images/sample-image3.png'
#  reading the images 
img = cv.imread(img_path)

denoised_img = cv.GaussianBlur(img, (3,3), 10)

edges_img = cv.Canny(denoised_img, 100,200)
dilate_img = cv.dilate(edges_img, (3,3), iterations=3)
contours, h = cv.findContours(dilate_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
sorted_box = sorted(contours, key=cv.boundingRect, reverse=False)
cv.putText(img, f'Sorted color Green ', (40, 20 ), cv.FONT_HERSHEY_PLAIN, 0.9, (0,255,0), 1, cv.LINE_AA)
cv.putText(img, f'Unsorted color Black ', (40, 35 ), cv.FONT_HERSHEY_PLAIN, 0.9, (0,0,0), 1, cv.LINE_AA)


for IDs, cnt  in enumerate(sorted_box):
    bbox = cv.boundingRect(cnt)
    # print(type(bbox))
    cv.rectangle(img, bbox, color=(0,0, 0), thickness=3)
    rect = cv.minAreaRect(cnt)
    # print(rect)
    box = cv.boxPoints(rect)
    # print(box)
    box = np.int0(box)
    cv.drawContours(img, [box], 0, (0,255, 0), 2)
    M = cv.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv.putText(img, f'{IDs}', (cx-10, cy ), cv.FONT_HERSHEY_PLAIN, 0.9, (0,255,0), 1, cv.LINE_AA)
    # cv.rectangle(img, box, color=(0, 255, 0),thickness=2 )
    cv.imshow('img', img)
    cv.waitKey(0)
for IDs, cnt  in enumerate(contours):
    bbox = cv.boundingRect(cnt)
    # print(type(bbox))
    cv.rectangle(img, bbox, color=(0,0, 0), thickness=3)
    rect = cv.minAreaRect(cnt)
    # print(rect)
    box = cv.boxPoints(rect)
    # print(box)
    box = np.int0(box)
    cv.drawContours(img, [box], 0, (0,255, 0), 2)
    M = cv.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv.putText(img, f' -> {IDs}', (cx, cy ), cv.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1, cv.LINE_AA)
    # cv.rectangle(img, box, color=(0, 255, 0),thickness=2 )
    cv.imshow('img', img)
    cv.waitKey(0)
cv.imshow('dilated_img', dilate_img)
# cv.imshow('img', img)
# cv.imshow('edges', edges_img)
cv.waitKey(0)
cv.destroyAllWindows()
