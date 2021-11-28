import cv2 as cv 
img = cv.imread('Images/sample_shapes.png')
denosied_img = cv.GaussianBlur(img, (3,3), 0)

# finding Edges 
edges_img = cv.Canny(denosied_img, 100, 130)
contours , h = cv.findContours(edges_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_TC89_L1)
for cnt in contours:
    epsilon = 0.06*cv.arcLength(cnt,True)
    approx = cv.approxPolyDP(cnt,epsilon,True)
    print(len(approx))
    M = cv.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv.putText(img, f'{len(approx)} Vertices', (cx-15, cy ), cv.FONT_HERSHEY_PLAIN, 0.9, (0,255,0), 1, cv.LINE_AA)
    cv.drawContours(img, cnt, -1, (0, 255,0), 3)
    cv.imshow('img', img)
    cv.waitKey(0)
cv.imshow('edges', edges_img)
cv.imshow('img', img)
cv.waitKey(0)

