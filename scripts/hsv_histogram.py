import cv2
import matplotlib.pyplot as plt
import os
from pathlib import Path

def plot_hsv_histogram(image_path, comment):
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    channels = ('Hue', 'Saturation', 'Value')
    colors = ('m', 'c', 'y')

    plt.figure(figsize=(10, 7))
    for i, col in enumerate(colors):
        plt.plot(cv2.calcHist([hsv], [i], None, [256], [0, 256]), color=col, label=channels[i])

    plt.title("HSV Histograms" + comment)
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.legend()
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


plot_hsv_histogram(image_path_1, " (yellow background)")
plot_hsv_histogram(image_path_2, " (brown/black banana)")
plot_hsv_histogram(image_path_3, " (yellow banana)")
plot_hsv_histogram(image_path_4, " (green banana)")
