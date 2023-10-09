import cv2 as cv
import numpy as np

# Definir los rangos de colores a detectar
colores = {
    "rojo": (np.array([0, 100, 100], dtype=np.uint8), np.array([10, 255, 255], dtype=np.uint8)),  # Rango rojo 1
    "rojo2": (np.array([170, 100, 100], dtype=np.uint8), np.array([180, 255, 255], dtype=np.uint8)),  # Rango rojo 2
    "verde": (np.array([35, 100, 100], dtype=np.uint8), np.array([77, 255, 255], dtype=np.uint8)),  # Rango verde
    "azul": (np.array([100, 100, 100], dtype=np.uint8), np.array([135, 255, 255], dtype=np.uint8)),  # Rango azul
    "amarillo": (np.array([25, 100, 100], dtype=np.uint8), np.array([35, 255, 255], dtype=np.uint8))  # Rango amarillo
}

# Iniciar la captura de video
cap = cv.VideoCapture(0)

# Obtener las dimensiones del video
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# Configurar el códec y crear el objeto VideoWriter
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('streaming.mp4', fourcc, 25.0, (width, height))

# Variable para contar los cuadros
frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convertir el cuadro a espacio de color HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Inicializar la máscara combinada
    combined_mask = np.zeros((height, width), dtype=np.uint8)

    for color, (lower, upper) in colores.items():
        # Crear una máscara para el rango de color actual
        mask = cv.inRange(hsv, lower, upper)

        # Aplicar operaciones morfológicas para mejorar la máscara
        mask = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((3, 3), np.uint8))
        mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, np.ones((9, 9), np.uint8))

        # Agregar la máscara actual a la máscara combinada
        combined_mask = cv.bitwise_or(combined_mask, mask)

        # Encontrar los contornos de la máscara actual
        contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        # Dibujar los contornos en el cuadro original
        cv.drawContours(frame, contours, -1, (0, 255, 0), 2)

    # Escribir el cuadro con los contornos en el archivo de video
    out.write(frame)

    # Incrementar el contador de cuadros
    frame_count += 1

    # Salir del bucle después de 1 minuto (25 cuadros por segundo)
    if frame_count == 1500:
        break

    # Mostrar el cuadro con los contornos
    cv.imshow("Video", frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
out.release()
cv.destroyAllWindows()
