#JOSUE DANIEL TORRES SANTOS
#VISION ARTIFICIAL
#23/05/23
#ACTIVIDAD 4 TRASNFORMACIONES GEOMETRICAS PART 1

import cv2
import  numpy as np

# Cargar la imagen
image = cv2.imread('douma.png')

# Escalar la imagen a la mitad de su tamaño original
scaled_image = cv2.resize(image, None, fx=0.5, fy=0.5)

# Rotar la imagen 45 grados en sentido antihorario
rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)


# Aplicar un efecto espejo horizontal
mirrored_image = cv2.flip(image, 1)


# Definir los puntos de la imagen original y los puntos de destino
original_points = np.float32([[0, 0], [image.shape[1] - 1, 0], [0, image.shape[0] - 1], [image.shape[1] - 1, image.shape[0] - 1]])
destination_points = np.float32([[50, 50], [image.shape[1] - 51, 50], [50, image.shape[0] - 51], [image.shape[1] - 51, image.shape[0] - 51]])

# Calcular la matriz de transformación
matrix = cv2.getPerspectiveTransform(original_points, destination_points)

# Aplicar la transformación de perspectiva a la imagen
perspective_transformed_image = cv2.warpPerspective(image, matrix, (image.shape[1], image.shape[0]))


cv2.imwrite("Escalado.png",scaled_image)
cv2.imwrite("Rotacion_45.png", rotated_image)
cv2.imwrite("Espejo.png" ,mirrored_image)
cv2.imwrite("Perspectiva.png", perspective_transformed_image)



# Crear el informe
report = """
--- Reporte ---

Imagen original:
Imagen 1:
![Imagen 1](douma.png)

Operaciones aritmeticas:
- Escalado:
![Escalado](Escalado.png)

- Rotacion:
![Rotacion](Rotacion_45.png)

- Espejo:
![Espejo](Espejo.png)

- Perspectiva:
![Perspectiva](Perspectiva.png)

"""

# Guardar el informe en un archivo
with open('reporte.md', 'w') as f:
    f.write(report)
