from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv
from google.colab.patches import cv2_imshow
from skimage import io

img_10_10 = np.zeros((10, 10), dtype=np.uint8)
vi = 0
inc = 12
for i in range(0, 10):
  v = vi
  for j in range(0, 10):
    img_10_10[i, j] = v
    v = v + inc
  vi = vi + inc

print(img_10_10)

plt.imshow(img_10_10, cmap="gray", vmin=0, vmax=255)
plt.show()
