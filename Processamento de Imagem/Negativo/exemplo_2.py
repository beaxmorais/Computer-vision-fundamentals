import numpy as np
import cv2 as cv
from google.colab.patches import cv2_imshow
from skimage import io

image_path = "/content/drive/MyDrive/Visão Computacional/"
image = io.imread(image_path + "breast.tif")

negativo = 255 - image
cv2_imshow(negativo)