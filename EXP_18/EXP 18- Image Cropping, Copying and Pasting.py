import cv2

img = cv2.imread("image.jpg")

h, w = img.shape[:2]

roi = img[20:120, 20:120]

img[h-120:h-20, w-120:w-20] = roi

cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
