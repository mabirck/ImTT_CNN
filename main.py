import cv2

im = cv2.imread('img\test.jpg')
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("Display window",WINDOW_AUTOSIZE)
cv.imshow("input",img)
