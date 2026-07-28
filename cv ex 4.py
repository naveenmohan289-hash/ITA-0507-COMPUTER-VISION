import cv2

# Read the image
image = cv2.imread("image.jpg")   # Replace with your image file

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale (Histogram Equalization works on single channel)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Histogram Equalization
    equalized = cv2.equalizeHist(gray)

    # Show original grayscale image
    cv2.imshow("Original Grayscale Image", gray)

    # Show equalized image
    cv2.imshow("Histogram Equalized Image", equalized)

    # Save the result (optional)
    cv2.imwrite("equalized_image.jpg", equalized)

    # Wait and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
