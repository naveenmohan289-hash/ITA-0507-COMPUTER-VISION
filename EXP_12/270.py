import cv2
import numpy as np

# Read the image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Rotate image 270 degrees clockwise (or 90 degrees counterclockwise)
rotated = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Save the output image
cv2.imwrite("rotated_image.jpg", rotated)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image (270° Clockwise)", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()