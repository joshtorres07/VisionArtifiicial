import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen original en escala de grises
imagen_original = cv2.imread("foto_deteccion.jpg")

# Agregar ruido a la imagen
imagen_con_ruido = np.copy(imagen_original)
ruido = np.random.normal(0, 50, imagen_con_ruido.shape).astype(np.uint8)  # Ajusta el parámetro de desviación estándar según desees
imagen_con_ruido += ruido

# Aplicar métodos de reducción de ruido
imagen_denoised1 = cv2.GaussianBlur(imagen_con_ruido, (3, 3), 0)
imagen_denoised2 = cv2.medianBlur(imagen_con_ruido, 3)
imagen_denoised3 = cv2.fastNlMeansDenoising(imagen_con_ruido, None, h=10, templateWindowSize=7, searchWindowSize=21)

# Guardar las imágenes generadas
cv2.imwrite("imagen_original_grises.png", imagen_original)
cv2.imwrite("imagen_con_ruido.png", imagen_con_ruido)
cv2.imwrite("imagen_denoised1.png", imagen_denoised1)
cv2.imwrite("imagen_denoised2.png", imagen_denoised2)
cv2.imwrite("imagen_denoised3.png", imagen_denoised3)

# Mostrar las imágenes en un reporte utilizando Matplotlib
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(imagen_original, cmap='gray')
plt.title('Imagen original')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(imagen_con_ruido, cmap='gray')
plt.title('Imagen con ruido')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(imagen_denoised1, cmap='gray')
plt.title('Denoised (GaussianBlur)')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(imagen_denoised2, cmap='gray')
plt.title('Denoised (medianBlur)')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(imagen_denoised3, cmap='gray')
plt.title('Denoised (fastNlMeansDenoising)')
plt.axis('off')

plt.tight_layout()
plt.show()
