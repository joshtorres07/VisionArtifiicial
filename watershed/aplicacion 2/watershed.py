import numpy as np
import cv2
from matplotlib import pyplot as plt
image = 'ejemplowater.jpg'

img = cv2.imread(image)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Eliminación del ruido
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Encuentra el área del fondo
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# Encuentra el área del primer
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

# Encuentra la región desconocida (bordes)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Etiquetado
ret, markers = cv2.connectedComponents(sure_fg)

# Adiciona 1 a todas las etiquetas para asegurra que el fondo sea 1 en lugar de cero
markers = markers + 1

# Ahora se marca la región desconocida con ceros
markers[unknown == 255] = 0
markers = cv2.watershed(img, markers)
img[markers == -1] = [255, 0, 0]

cv2.imwrite("binarizada.jpg", thresh)
cv2.imwrite("sin ruido.jpg", opening)
cv2.imwrite("area de fondo.jpg", sure_bg)
cv2.imwrite("area de frente.jpg", sure_fg)
cv2.imwrite("distancia.jpg", dist_transform)
cv2.imwrite("bordes.jpg", unknown)
cv2.imwrite("regiones.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

