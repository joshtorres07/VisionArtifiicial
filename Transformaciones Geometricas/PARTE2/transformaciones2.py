#JOSUE DANIEL TORRES SANTOS
#VISION ARTIFICIAL
#23/05/23
#ACTIVIDAD 4 TRASNFORMACIONES GEOMETRICAS PARTE 2
import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('akazabb.png')

# Definir la primera transformación: Escalado
scale_factor = 0.5
scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)

# Definir la segunda transformación: Rotación
angle = 45
rows, cols, _ = scaled_image.shape
rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
rotated_image = cv2.warpAffine(scaled_image, rotation_matrix, (cols, rows))

# Definir la tercera transformación: Espejo horizontal
mirrored_image = cv2.flip(rotated_image, 1)

# Definir la cuarta transformación: Espejo vertical
flipped_image = cv2.flip(mirrored_image, 0)

# Definir la quinta transformación: Desplazamiento
x_offset = 50
y_offset = 50
rows, cols, _ = flipped_image.shape
translation_matrix = np.float32([[1, 0, x_offset], [0, 1, y_offset]])
translated_image = cv2.warpAffine(flipped_image, translation_matrix, (cols, rows))

# Mostrar la imagen resultante de todas las transformaciones
cv2.imshow("Imagen resultante", translated_image)
cv2.imwrite("Imagen resultante.png", translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""# Cargar la imagen
image = cv2.imread('akazabb.png')

# Ajustar el contraste y brillo de la imagen
alpha = 1.5  # factor de contraste
beta = 50  # factor de brillo
adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Cargar la imagen en escala de grises
gray_image = cv2.imread('imagen.jpg', 0)

# Aplicar el algoritmo Canny para detección de bordes
edges = cv2.Canny(gray_image, 100, 200)

# Definir el kernel para la operación morfológica
kernel = np.ones((5, 5), np.uint8)

# Aplicar dilatación a la imagen
dilated_image = cv2.dilate(gray_image, kernel, iterations=1)

# Aplicar erosión a la imagen
eroded_image = cv2.erode(gray_image, kernel, iterations=1)"""