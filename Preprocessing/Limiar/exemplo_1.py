# Limiarizar a imagem
import numpy as np
import cv2 as cv
from google.colab.patches import cv2_imshow
from skimage import io

image_path = "/content/drive/MyDrive/Visão Computacional/"
image = cv.cvtColor(io.imread(image_path + "coins.jpg"), cv.COLOR_RGBA2GRAY)

len = image.shape

for i in range(0, 501):
  for j in range(0, 391):
    if image[i][j] < 128:
      image[i][j] = 0
    else:
      image[i][j] = 255

cv2_imshow(image)
