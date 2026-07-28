# Import OpenCV
import cv2

# Read the image
image = cv2.imread("image.jpg")   # Replace with your image file

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Display original image
    cv2.imshow("Original Image", image)

    # Convert to grayscale (required for Canny)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blurred, 100, 200)

    # Display edges (outline)
    cv2.imshow("Canny Edge Detection (Outline)", edges)

    # Save the output image (optional)
    cv2.imwrite("edges_image.jpg", edges)

    # Wait for key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
