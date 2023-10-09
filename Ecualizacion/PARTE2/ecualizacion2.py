import cv2
import matplotlib.pyplot as plt

# Cargar la imagen a color
image = cv2.imread('shoto.png')

# Separar la imagen en los tres canales: BGR
b, g, r = cv2.split(image)
cv2.imwrite("b.png", b)
cv2.imwrite("g.png", g)
cv2.imwrite("r.png", r)
# Generar y guardar el histograma de cada canal
b_hist = cv2.calcHist([b], [0], None, [256], [0, 256])
g_hist = cv2.calcHist([g], [0], None, [256], [0, 256])
r_hist = cv2.calcHist([r], [0], None, [256], [0, 256])

plt.plot(b_hist, color='b')
plt.title('Histograma del canal Azul (B)')
plt.savefig('b_histogram.png')
plt.close()

plt.plot(g_hist, color='g')
plt.title('Histograma del canal Verde (G)')
plt.savefig('g_histogram.png')
plt.close()

plt.plot(r_hist, color='r')
plt.title('Histograma del canal Rojo (R)')
plt.savefig('r_histogram.png')
plt.close()

# Ecualizar cada canal por separado
b_eq = cv2.equalizeHist(b)
g_eq = cv2.equalizeHist(g)
r_eq = cv2.equalizeHist(r)

# Unir los canales ecualizados
equ_image = cv2.merge([b_eq, g_eq, r_eq])

# Guardar la imagen ecualizada
cv2.imwrite('equ_image.jpg', equ_image)

# Generar y guardar el histograma de la imagen ecualizada
equ_hist = cv2.calcHist([equ_image], [0], None, [256], [0, 256])
plt.plot(equ_hist, color='m')
plt.title('Histograma de la imagen ecualizada')
plt.savefig('equ_histogram.png')
plt.close()

# Generar el reporte
report = """
--- Reporte ---


--- Reporte ---

Imagen a color original:
![Imagen a color original](shoto.png)

Imagen en el canal azul:
![Imagen en el canal azul](b.png)

Imagen en el canal rojo:
![Imagen en el canal rojo](r.png)

Imagen en el canal verde:
![Imagen en el canal verde](g.png)

Histograma del canal Azul (B):
![Histograma del canal Azul (B)](b_histogram.png)

Histograma del canal Verde (G):
![Histograma del canal Verde (G)](g_histogram.png)

Histograma del canal Rojo (R):
![Histograma del canal Rojo (R)](r_histogram.png)

Imagen ecualizada:
![Imagen ecualizada](equ_image.jpg)

Histograma de la imagen ecualizada:
![Histograma de la imagen ecualizada](equ_histogram.png)

"""

# Guardar el reporte en un archivo
with open('reporte.md', 'w') as f:
    f.write(report)
