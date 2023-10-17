# Normalização da imagem
image_path = "/content/drive/MyDrive/Visão Computacional/"
image = io.imread(image_path + "beans.tif")

equ_image = cv.equalizeHist(image)
cv2_imshow(equ_image)

counts = np.zeros(256).astype(int)
bins = np.array(range(0, 256))

#print(bins)

for i in bins:

  counts[i] = image[image == i].shape[0]
  #print(image[image == i].shape[0])
plt.bar(bins, counts)

plt.show()