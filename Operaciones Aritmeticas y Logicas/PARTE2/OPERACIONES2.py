import cv2

# Cargar las dos imágenes
image1 = cv2.imread('aphelios.png')
image2 = cv2.imread('sett.png')

height, width, _ = image1.shape

# Redimensionar la imagen2 para que tenga las mismas dimensiones que image1
image2 = cv2.resize(image2, (width, height))

# Especificar los pesos para cada imagen
weight_image1 = 0.6
weight_image2 = 0.4

# Realizar la combinación de imágenes
blended_image = cv2.addWeighted(image1, weight_image1, image2, weight_image2, 0)

# Guardar la imagen resultante
cv2.imwrite('imagen_combinada.jpg', blended_image)
