import cv2

# Read the image
img = cv2.imread("C:/Users/AMUTHAVAN/OneDrive/Desktop/cv/images.png")

# Check whether the image is loaded
if img is None:
    print("Error: Image not found")
else:
    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(img, (15, 15), 0)

    # Display the original and blurred images
    cv2.imshow("Original Image", img)
    cv2.imshow("Gaussian Blur Image", blur)

    # Wait for a key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()
