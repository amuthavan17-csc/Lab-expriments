import cv2

# Read the image
img = cv2.imread("C:/Users/AMUTHAVAN/OneDrive/Desktop/cv/images.png")

# Check whether the image is loaded
if img is None:
    print("Error: Image not found")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect edges using Canny
    edges = cv2.Canny(gray, 100, 200)

    # Display the original and outline images
    cv2.imshow("Original Image", img)
    cv2.imshow("Image Outline", edges)

    # Wait for a key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()
