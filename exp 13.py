
import cv2
import numpy as np

# Read the image
img = cv2.imread("C:/Users/AMUTHAVAN/OneDrive/Desktop/cv/images.png")

if img is None:
    print("Error: Image not found")
else:
    rows, cols = img.shape[:2]

    # Define three points in the original image
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

    # Define corresponding points in the transformed image
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    # Calculate affine transformation matrix
    matrix = cv2.getAffineTransform(pts1, pts2)

    # Apply affine transformation
    transformed = cv2.warpAffine(img, matrix, (cols, rows))

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Affine Transformed Image", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
