import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_color_histogram(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Image not found!")
        return
    
    # Split the image into B, G, R channels
    channels = cv2.split(image)
    colors = ('b', 'g', 'r')
    
    # Plot histogram for each channel
    plt.figure()
    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity Value")
    plt.ylabel("Number of Pixels")
    
    for channel, color in zip(channels, colors):
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    
    # Show the image
    cv2.imshow("Input Image", image)
    
    # Show histogram
    plt.show()
    
    # Wait and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function
analyze_color_histogram("image.jpg")   # Replace with your image file
