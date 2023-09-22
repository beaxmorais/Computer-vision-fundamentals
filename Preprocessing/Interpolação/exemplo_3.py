# Interpolação bicubica
resized_bicubica = cv.resize(img_10_10, (20,20), interpolation=cv.INTER_CUBIC)

plt.imshow(resized_bicubica, cmap="gray", vmin=0, vmax=255)
plt.show()