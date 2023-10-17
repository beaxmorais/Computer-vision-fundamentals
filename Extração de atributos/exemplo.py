import numpy as np
import cv2 as cv
import mahotas as mt
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow # for image display
from skimage import io

image_path = "/content/drive/MyDrive/Visão Computacional/"

image = io.imread(image_path + "lena.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
cv2_imshow(cv.resize(image, None, fx=.52, fy=.52))