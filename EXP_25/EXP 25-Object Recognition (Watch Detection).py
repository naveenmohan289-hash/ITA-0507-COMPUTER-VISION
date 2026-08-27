import cv2

img = cv2.imread("watch.jpg")

cv2.imshow("Watch Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
