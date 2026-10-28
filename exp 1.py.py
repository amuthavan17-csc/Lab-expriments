import cv2

# Read the image
image = cv2.imread('C:/Users/AMUTHAVAN/OneDrive/Desktop/cv/images.png')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite('gray_image.jpg', gray_image)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
