import cv2
import numpy as np


def obtener_esqueleto(imagen):
    # Convertir la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar umbral binario a la imagen
    _, umbral = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY_INV)

    # Aplicar el algoritmo de adelgazamiento
    esqueleto = adelgazamiento(umbral)

    return esqueleto


def adelgazamiento(imagen):
    # Definir el kernel estructurante para el algoritmo de adelgazamiento
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

    # Inicializar una matriz de ceros del mismo tamaño que la imagen
    adelgazada = np.zeros(imagen.shape, np.uint8)

    # Aplicar el algoritmo de adelgazamiento hasta que la imagen no cambie
    while True:
        erosion = cv2.erode(imagen, kernel)
        apertura = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
        sub = cv2.subtract(erosion, apertura)
        adelgazada = cv2.bitwise_or(adelgazada, sub)
        imagen = erosion.copy()

        if cv2.countNonZero(imagen) == 0:
            break

    return adelgazada


# Cargar la imagen de entrada
imagen_entrada = cv2.imread("douma.png")

# Obtener el esqueleto de la imagen de entrada
esqueleto = obtener_esqueleto(imagen_entrada)

# Mostrar la imagen de entrada y el esqueleto
cv2.imshow("Imagen de entrada", imagen_entrada)
cv2.imshow("Esqueleto", esqueleto)
cv2.waitKey(0)
cv2.destroyAllWindows()
