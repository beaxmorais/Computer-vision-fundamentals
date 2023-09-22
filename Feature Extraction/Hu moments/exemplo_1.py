import cv2 as cv
from google.colab.patches import cv2_imshow

lena = cv.cvtColor(io.imread(image_path + "lena.jpg"), cv.COLOR_RGBA2GRAY)

# Média
m1 = sum(sum(lena))/lena.size

#Desvio padrão
m2 = (sum(sum((lena - m1)**2))/lena.size)**(1/2)

# Obliquidade
m3 = (sum(sum((lena - m1)**3))/lena.size)**(1/3)

# Curtose
m4 = (sum(sum((lena - m1)**4))/lena)**(1/4)

# Vetor que descreve a lena
v = [m1, m2, m3, m4]

# Momentos de Hu da Lena
hu_moments = cv.HuMoments(cv.moments(lena)).flatten()

# Lena 180º
img_rotate = cv.rotate(lena, cv.ROTATE_180)

# Momentos de Hu Lena 180º
hu_180_moments = cv.HuMoments(cv.moments(img_rotate)).flatten()

final_frame = cv.hconcat((lena, img_rotate))
cv2_imshow(final_frame)


print(hu_moments, '\n', hu_180_moments)
print("Vetor de característica: ", v)
