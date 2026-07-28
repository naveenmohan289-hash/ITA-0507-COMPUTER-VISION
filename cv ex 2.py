# Import OpenCV library
import cv2

# Read the image
image = cv2.imread("image.jpg")   # Replace with your image file name

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Display original image
    cv2.imshow("Original Image", image)

    # Apply Gaussian Blur
    # (5,5) is the kernel size, 0 means auto-calculated sigma
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Display blurred image
    cv2.imshow("Gaussian Blurred Image", blurred_image)

    # Save the blurred image (optional)
    cv2.imwrite("blurred_image.jpg", blurred_image)

    # Wait for key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
