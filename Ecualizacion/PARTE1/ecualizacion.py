#JOSUE DANIEL TORRES SANTOS
#VISION ARTIFICIAL
#ACTIVIDAD 7 ECUALIZACION
#23-05-23

import cv2
import matplotlib.pyplot as plt
    
# Cargar la imagen PNG
image = cv2.imread('rengoku.png')

# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Guardar la imagen en escala de grises
cv2.imwrite("rengoku_gray.png", gray_image)

# Generar y guardar el histograma de la imagen en escala de grises
gray_hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
plt.plot(gray_hist)
plt.title('Histograma de la imagen en escala de grises')
plt.savefig('gray_histogram.png')
plt.close()

# Ecualizar la imagen
equ_image = cv2.equalizeHist(gray_image)

# Guardar la imagen ecualizada
cv2.imwrite('equ_image.jpg', equ_image)

# Generar y guardar el histograma de la imagen ecualizada
equ_hist = cv2.calcHist([equ_image], [0], None, [256], [0, 256])
plt.plot(equ_hist)
plt.title('Histograma de la imagen ecualizada')
plt.savefig('equ_histogram.png')
plt.close()

# Generar el reporte
report = """
--- Reporte ---

Imagen en escala de grises:
![Imagen en escala de grises](rengoku_gray.png)

Histograma de la imagen en escala de grises:
![Histograma de la imagen en escala de grises](gray_histogram.png)

Imagen ecualizada:
![Imagen ecualizada](equ_image.jpg)

Histograma de la imagen ecualizada:
![Histograma de la imagen ecualizada](equ_histogram.png)
"""

# Guardar el reporte en un archivo
with open('reporte.md', 'w') as f:
    f.write(report)
