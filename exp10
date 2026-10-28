import cv2

img = cv2.imread("C:/Users/AMUTHAVAN/OneDrive/Desktop/cv/images.png")

if img is None:
    print("Error: Image not found")
else:
 
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
