# Interpolação bilinear
resized_bilinear = cv.resize(img_10_10, (20,20), interpolation=cv.INTER_LINEAR)

plt.imshow(resized_bilinear, cmap="gray", vmin=0, vmax=255)
plt.show()