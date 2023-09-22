# Comparação de histogramas com imagem equalizada
image_path = "/content/drive/MyDrive/Visão Computacional/"
image = cv.cvtColor(io.imread(image_path + "lena.jpg"), cv.COLOR_RGBA2GRAY)

equ_image = cv.equalizeHist(image)

counts = np.zeros(256).astype(int)
bins = np.array(range(0, 256))

for i in bins:
  counts[i] = len(equ_image[i == equ_image])


plt.bar(bins, counts)
plt.show

final_frame = cv.hconcat((image, equ_image))

original_image = image.copy()

counts = np.zeros(256).astype(int)
bins = np.array(range(0, 256))

for i in bins:
  counts[i] = len(original_image[original_image == i])

plt.bar(bins, counts)
plt.show

final_frame = cv.hconcat((original_image, equ_image))
