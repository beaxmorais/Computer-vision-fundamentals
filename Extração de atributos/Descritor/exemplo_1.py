import cv2 as cv
from google.colab.patches import cv2_imshow

image_gray = cv.cvtColor(io.imread(image_path + "lena.jpg"), cv.COLOR_RGBA2GRAY)

# Média
m1 = sum(sum(image_gray))/image_gray.size
print("Média: ", m1)

# Desvio padrão
m2 = (sum(sum((image_gray - m1)**2))/image_gray.size)**(1/2)
print("Desvio padrão: ", m2)

# Obliquidade
m3 = (sum(sum((image_gray - m1)**3))/image_gray.size)**(1/3)
print("Obliquidade: ", m3)

# Curtose
m4 = (sum(sum((image_gray - m1)**4))/image_gray.size)**(1/4)
print("Curtose: ", m4)

print("")

# Vetor de característica
v = [m1, m2, m3, m4]
print("Vetor de característica: ", v)