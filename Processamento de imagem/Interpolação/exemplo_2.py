from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv
from google.colab.patches import cv2_imshow
from skimage import io

for i in range(0, 20):
  for j in range(0, 18):
      img_20_20[i][j] = int((img_20_20[i][j] + img_20_20[i][j+2])/2)

plt.imshow(img_20_20, cmap="gray", vmin=0, vmax=255)
plt.show()

image_path = "/content/drive/MyDrive/Visão Computacional/"
image = io.imread(image_path + "coins.jpg")
image_3 = cv.cvtColor(image, cv.COLOR_RGBA2GRAY)
cv2_imshow(image_3)