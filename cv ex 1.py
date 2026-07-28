# Import OpenCV library
import cv2

# Read the image
image = cv2.imread("image.jpg")   # Replace 'image.jpg' with your image file name

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    # Display the original image
    cv2.imshow("Original Image", image)

    # Convert the image to Gray-scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the Gray-scale image
    cv2.imshow("Gray-scale Image", gray_image)

    # Save the Gray-scale image (optional)
    cv2.imwrite("gray_image.jpg", gray_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
