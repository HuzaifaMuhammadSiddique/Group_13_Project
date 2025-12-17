import cv2
import matplotlib.pyplot as plt
import os

def plot_hsv_histogram(image_path):
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    channels = ('Hue', 'Saturation', 'Value')
    colors = ('m', 'c', 'y')

    plt.figure(figsize=(10, 7))
    for i, col in enumerate(colors):
        plt.plot(cv2.calcHist([hsv], [i], None, [256], [0, 256]), color=col, label=channels[i])

    plt.title("HSV Histograms")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()

# Example:
# print("Working directory:", os.getcwd())
# print("File exists:", os.path.exists("./dataset/dev/Sagor_Kola_3_jpg.rf.d4c6b2ba6ca2d30eb1179249eb647afe.jpg"))

# plot_hsv_histogram(r"./dataset/dev/Raw_Banana.4dbd0091-ebe4-11ed-9751-346f24e2fa38.jpg")

extention = ".jpeg"
extention2 = '.jpg'
name = "banana_dev_"
path = './dataset/dev/'

# for i in range(1,10,1):
#     new_name = name + "000" + str(i) + extention
#     print(new_name)
#     new_path = path + new_name
#     print(new_path)
#     plot_hsv_histogram(new_path)

# for i in range(10, 19, 1):
#     new_name = name + "00" + str(i) + extention
#     new_path = path + new_name
#     plot_hsv_histogram(new_path)

# for i in range(19, 100, 1):
#     new_name = name + "00" + str(i) + extention2
#     new_path = path + new_name
#     plot_hsv_histogram(new_path)

plot_hsv_histogram("./dataset/dev/banana_dev_0946.jpg")