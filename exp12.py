import cv2

# Read the image
img = cv2.imread("C:/Users/AMUTHAVAN/OneDrive/Desktop/cv/images.png")

if img is None:
    print("Error: Image not found")
else:
    # Rotate 270 degrees clockwise
    rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image 270 Degrees", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
