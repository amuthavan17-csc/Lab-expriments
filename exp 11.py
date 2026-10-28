import cv2

# Read the image
img = cv2.imread("C:/Users/AMUTHAVAN/OneDrive/Desktop/cv/images.png")

if img is None:
    print("Error: Image not found")
else:
    # Rotate the image 180 degrees
    rotated = cv2.rotate(img, cv2.ROTATE_180)

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image 180 Degrees", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
