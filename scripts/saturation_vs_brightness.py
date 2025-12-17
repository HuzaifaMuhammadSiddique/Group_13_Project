import numpy as np
import cv2
import matplotlib.pyplot as plt

def plot_saturation_vs_brightness(image_path):
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    H, S, V = cv2.split(hsv)

    plt.figure(figsize=(8, 6))
    plt.scatter(S.flatten(), V.flatten(), s=1, color='green')
    plt.xlabel("Saturation (S)")
    plt.ylabel("Brightness (Value, V)")
    plt.title("Saturation vs Brightness")
    plt.show()

extention = "jpeg"
extention2 = 'jpg'
name = "banana_dev_"
path = './dataset/dev/'

for i in range(1,10,1):
    new_name = name + str(i) + extention
    new_path = path + name
    plot_saturation_vs_brightness(new_path)
