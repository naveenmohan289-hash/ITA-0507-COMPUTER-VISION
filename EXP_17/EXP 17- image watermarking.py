import cv2

img = cv2.imread("image.jpg")

watermark = img.copy()
cv2.putText(watermark, "WATERMARK", (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

result = cv2.addWeighted(img, 0.8, watermark, 0.2, 0)

cv2.imshow("Original", img)
cv2.imshow("Watermarked", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
