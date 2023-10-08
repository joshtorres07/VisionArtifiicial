import cv2

# Cargar las dos imágenes
image1 = cv2.imread('aphelios.png')
image2 = cv2.imread('sett.png')

# Obtener las dimensiones de la imagen1
height, width, _ = image1.shape

# Redimensionar la imagen2 para que tenga las mismas dimensiones que image1
image2 = cv2.resize(image2, (width, height))

# Sumar las imágenes
sum_image = cv2.add(image1, image2)

# Guardar la imagen resultante
cv2.imwrite('suma_imagenes.jpg', sum_image)

# Resta de imágenes
diff_image = cv2.subtract(image1, image2)
cv2.imwrite('resta_imagenes.jpg', diff_image)

# Multiplicación de imágenes
mul_image = cv2.multiply(image1, image2)
cv2.imwrite('multiplicacion_imagenes.jpg', mul_image)

# Operación bitwise AND
bitwise_and_image = cv2.bitwise_and(image1, image2)
cv2.imwrite('bitwise_and_imagenes.jpg', bitwise_and_image)

# Operación bitwise OR
bitwise_or_image = cv2.bitwise_or(image1, image2)
cv2.imwrite('bitwise_or_imagenes.jpg', bitwise_or_image)

# Operación bitwise XOR
bitwise_xor_image = cv2.bitwise_xor(image1, image2)
cv2.imwrite('bitwise_xor_imagenes.jpg', bitwise_xor_image)

# Crear el informe
report = """
--- Reporte ---

Imagenes originales:
Imagen 1:
![Imagen 1](aphelios.png)

Imagen 2:
![Imagen 2](sett.png)

Operaciones aritmeticas:
- Suma de imagenes:
![Suma de imagenes](suma_imagenes.jpg)

- Resta de imagenes:
![Resta de imagenes](resta_imagenes.jpg)

- Multiplicacion de imagenes:
![Multiplicacion de imagenes](multiplicacion_imagenes.jpg)

Operaciones a nivel de bits:
- Operación bitwise AND:
![Operación bitwise AND](bitwise_and_imagenes.jpg)

- Operación bitwise OR:
![Operación bitwise OR](bitwise_or_imagenes.jpg)

- Operación bitwise XOR:
![Operación bitwise XOR](bitwise_xor_imagenes.jpg)
"""

# Guardar el informe en un archivo
with open('reporte.md', 'w') as f:
    f.write(report)
