import cv2

# Read the image
img = cv2.imread("C:/Users/AMUTHAVAN/OneDrive/Desktop/cv/images.png")

if img is None:
    print("Error: Image not found")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization
    equalized = cv2.equalizeHist(gray)

    # Display original and equalized images
    cv2.imshow("Original Image", gray)
    cv2.imshow("Histogram Equalized Image", equalized)

    # Wait for a key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()
