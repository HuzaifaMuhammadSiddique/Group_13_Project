import cv2
import matplotlib.pyplot as plt

def plot_rgb_histogram(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    colors = ('r', 'g', 'b')
    plt.figure(figsize=(10, 5))
    plt.title("RGB Histogram")
    plt.xlabel("Pixel Intensity (0–255)")
    plt.ylabel("Frequency")

    for i, col in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    
    plt.show()

# Example:
plot_rgb_histogram(".\dataset\dev\Sagor_Kola_517_jpg.rf.d6a532fac8a1e4550be9fc05170bd8d4.jpg")
