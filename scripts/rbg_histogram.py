import cv2
import matplotlib.pyplot as plt
from pathlib import Path

def plot_rgb_histogram(image_path, comment):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    colors = ('r', 'g', 'b')
    plt.figure(figsize=(10, 5))
    plt.title("RGB Histogram" + comment)
    plt.xlabel("Pixel Intensity (0–255)")
    plt.ylabel("Frequency")

    for i, col in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    
    plt.show()

SCRIPT_DIR = Path(__file__).resolve().parent

# banana image with yellow background (out of the scope of the project) 
image_path_1 = SCRIPT_DIR.parent / "data" / "dev" / "banana_dev_0002.jpeg"

# banana image that is mostly brown/black 
image_path_2 = SCRIPT_DIR.parent / "data" / "dev" / "banana_dev_0118.jpg"

# banana image that is mostly yellow
image_path_3 = SCRIPT_DIR.parent / "data" / "dev" / "banana_dev_0806.jpg"

# banana image that is mostly green
image_path_4 = SCRIPT_DIR.parent / "data" / "dev" / "banana_dev_1127.jpg"


plot_rgb_histogram(image_path_1, " (yellow background)")
plot_rgb_histogram(image_path_2, " (brown/black banana)")
plot_rgb_histogram(image_path_3, " (yellow banana)")
plot_rgb_histogram(image_path_4, " (green banana)")
