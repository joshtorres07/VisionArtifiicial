#JOSUE DANIEL TORRES SANTOS
#VISION ARTIFICIAL
#23/05/23
#OPERACIONES INDIVIDUALES

import cv2 as cv
import numpy as np
"""
    Programa que funciona para imágenes en blanco y negro
"""

imagen1 = cv.imread('vision_yo.png',0)

inversa = imagen1.copy()

for f, c in np.ndindex(imagen1.shape):
    inversa[f, c] = 255-imagen1[f, c]

umbral = imagen1.copy()

for f, c in np.ndindex(imagen1.shape):
    if imagen1[f, c] <= 100:
        umbral[f, c] = 0
    elif imagen1[f, c] > 100:
        umbral[f, c] = 255

uI = imagen1.copy()
for f, c in np.ndindex(imagen1.shape):
    if imagen1[f, c] <= 100:
        uI[f, c] = 255
    elif imagen1[f, c] > 100:
        uI[f, c] = 0

p1 = 150
p2 = 220

u = imagen1.copy()
for f, c in np.ndindex(imagen1.shape):
    if p1 < imagen1[f, c] and imagen1[f, c] < p2:
        u[f, c] = 0
    elif imagen1[f, c] <= p1 or imagen1[f, c] >= p2:
        u[f, c] = 255

p1 = 50
p2 = 150

uIA = imagen1.copy()
for f, c in np.ndindex(imagen1.shape):
    if p1 < imagen1[f, c] and imagen1[f, c] < p2:
        uI[f, c] = 255
    elif imagen1[f, c] <= p1 or imagen1[f, c] >= p2:
        uI[f, c] = 0

p1 = 150
p2 = 220

uG = imagen1.copy()
for f, c in np.ndindex(imagen1.shape):
    if p1 < imagen1[f, c] and imagen1[f, c] < p2:
        uG[f, c] = imagen1[f, c]
    elif imagen1[f, c] <= p1 or imagen1[f, c] >= p2:
        uG[f, c] = 255

p1 = 150
p2 = 220

uGI = imagen1.copy()
for f, c in np.ndindex(imagen1.shape):
    if p1 < imagen1[f, c] and imagen1[f, c] < p2:
        uGI[f, c] = 255-imagen1[f, c]
    elif imagen1[f, c] <= p1 or imagen1[f, c] >= p2:
        uGI[f, c] = 255

p1 = 50
p2 = 150

extendida = imagen1.copy()
for f, c in np.ndindex(imagen1.shape):
    if p1 < imagen1[f, c] and imagen1[f, c] < p2:
        extendida[f, c] = (imagen1[f, c]-p1)*(255/(p2-p1))
    elif imagen1[f, c] <= p1 or imagen1[f, c] >= p2:
        extendida[f, c] = 0

p1 = 50
p2 = 150

reduccion = imagen1.copy()
for f, c in np.ndindex(imagen1.shape):
    if imagen1[f, c] <= 50:
        reduccion[f, c] = 0
    elif 50 < imagen1[f, c] and imagen1[f, c] <= 100:
        reduccion[f, c] = 32
    elif 100 < imagen1[f, c] and imagen1[f, c] <= 150:
        reduccion[f, c] = 64
    elif 150 < imagen1[f, c] and imagen1[f, c] <= 200:
        reduccion[f, c] = 128
    elif 200 < imagen1[f, c] and imagen1[f, c] <= 255:
        reduccion[f, c] = 255


cv.imwrite("a_Colorn't.png", imagen1)
cv.imwrite("b_Colorn't.png", inversa)
cv.imwrite("c_Colorn't.png", umbral)
cv.imwrite("d_Colorn't.png", uI)
cv.imwrite("e_Colorn't.png", u)
cv.imwrite("e.1_Color.png", uIA)
cv.imwrite("f_Colorn't.png", uG)
cv.imwrite("g_Colorn't.png", uGI)
cv.imwrite("h_Colorn't.png", extendida)
cv.imwrite("i_Colorn't.png", reduccion)