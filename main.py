import cv2

im = cv2.imread('img/test.jpg',1)
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("Colorfull image",cv2.WINDOW_NORMAL)
cv2.namedWindow("Gray image",cv2.WINDOW_NORMAL)
cv2.imshow("Colorfull image",im)
cv2.imshow("Gray image",img)
cv2.waitKey(0)
