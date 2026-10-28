
import cv2

# Read the input image
img = cv2.imread("C:/Users/AMUTHAVAN/OneDrive/Desktop/cv/images.png")

if img is None:
    print("Error: Image not found")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Sobel filter in X direction
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

    # Apply Sobel filter in Y direction
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # Convert results to 8-bit images
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)

    # Combine both Sobel results
    sobel = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Sobel X", sobel_x)
    cv2.imshow("Sobel Y", sobel_y)
    cv2.imshow("Sobel Filtered Image", sobel)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
