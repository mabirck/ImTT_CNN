import cv2

im = cv2.imread('img/test.jpg',1)
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("Display window",cv2.WINDOW_NORMAL)
cv2.imshow("Display window",img)
cv2.waitKey(0)
