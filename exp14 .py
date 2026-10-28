
import cv2
import numpy as np

# Read the image
img = cv2.imread("C:/Users/AMUTHAVAN/OneDrive/Desktop/cv/images.png")

if img is None:
    print("Error: Image not found")
else:
    rows, cols = img.shape[:2]

    # Define four points in the original image
    pts1 = np.float32([
        [50, 50],
        [cols - 50, 50],
        [50, rows - 50],
        [cols - 50, rows - 50]
    ])

    # Define four points in the transformed image
    pts2 = np.float32([
        [0, 0],
        [cols, 0],
        [50, rows],
        [cols - 50, rows]
    ])

    # Calculate perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply perspective transformation
    transformed = cv2.warpPerspective(
        img, matrix, (cols, rows)
    )

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Perspective Transformed Image", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
