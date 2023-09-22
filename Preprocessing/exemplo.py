import numpy as np
import cv2 as cv
from google.colab.patches import cv2_imshow
from skimage import io

image_path = "/content/drive/MyDrive/Visão Computacional/"
image = io.imread(image_path + "lena.jpg")
image_2 = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image_3 = cv.cvtColor(image, cv.COLOR_RGBA2GRAY)
final_frame = cv.hconcat((image, image_2))
cv2_imshow(final_frame)
cv2_imshow(cv.resize(image_3, None, fx=.52, fy=.51))

print("Tamanho: ", image.shape)
print("Tamanho RGB: ", image_2.shape)
print("Tamanho cinze: ", image_3.shape)

print("Tipo de pixels: ", image_3.dtype)
print("Pixels: ", image_3)

#Slice 
image_grid = image_3.copy()
image_grid[::50,:] = 255
image_grid[:,::50] = 255
cv2_imshow(cv.resize(image_grid, None, fx=.52, fy=.52))