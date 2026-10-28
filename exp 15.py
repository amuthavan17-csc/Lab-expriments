
import cv2
import numpy as np

# Read the image
img = cv2.imread("C:/Users/AMUTHAVAN/OneDrive/Desktop/cv/images.png")

if img is None:
    print("Error: Image not found")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert grayscale image to float32
    gray = np.float32(gray)

    # Apply Harris Corner Detection
    corners = cv2.cornerHarris(gray, 2, 3, 0.04)

    # Dilate the corners for better visibility
    corners = cv2.dilate(corners, None)

    # Mark detected corners in red
    img[corners > 0.01 * corners.max()] = [0, 0, 255]

    # Display the result
    cv2.imshow("Harris Corner Detection", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
