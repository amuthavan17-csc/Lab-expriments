
import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    # Read the input image
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found")
        return

    # Convert BGR to RGB for correct display
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Display the original image
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(rgb)
    plt.title("Original Image")
    plt.axis("off")

    # Calculate and plot color histograms
    colors = ('b', 'g', 'r')
    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.subplot(1, 2, 2)
        plt.plot(hist, color=color)
    
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity (0-255)")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.tight_layout()
    plt.show()

# Call the function
analyze_histogram("C:/Users/AMUTHAVAN/OneDrive/Desktop/cv/images.png")
