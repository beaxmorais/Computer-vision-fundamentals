# Comparação de histogramas
image_path = "/content/drive/MyDrive/Visão Computacional/"
image = cv.cvtColor(io.imread(image_path + "coins.jpg"), cv.COLOR_RGBA2GRAY)

desloca_image = image.copy()
desloca_image = desloca_image + 50

counts = np.zeros(256).astype(int)
bins = np.array(range(0, 256))

for i in bins:
  counts[i] = len(desloca_image[i == desloca_image])


plt.bar(bins, counts)
plt.show

final_frame = cv.hconcat((image, desloca_image))

original_image = image.copy()

counts = np.zeros(256).astype(int)
bins = np.array(range(0, 256))

for i in bins:
  counts[i] = len(original_image[original_image == i])

plt.bar(bins, counts)
plt.show

final_frame = cv.hconcat((original_image, desloca_image))

cv2_imshow(final_frame)