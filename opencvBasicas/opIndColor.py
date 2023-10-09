#JOSUE DANIEL TORRES SANTOS
#VISION ARTIFICIAL
#23/05/23
#OPERACIONES BASICAS CON OPENCV

from re import U
import cv2 as cv
import numpy as np
"""
    Programa que funciona para imágenes en blanco y negro
    Si se quiere usar a color es necesario:
"""

imagen1 = cv.imread('vision_yo.png')

inversa = imagen1.copy()

for f, c, x in np.ndindex(imagen1.shape):
    inversa[f, c, x] = 255-imagen1[f, c, x]

umbral = imagen1.copy()

for f, c, x in np.ndindex(imagen1.shape):
#for f, c in np.ndindex(imagen1.shape):
    if imagen1[f, c, x] <= 100:
        umbral[f, c, x] = 0
    elif imagen1[f, c, x] > 100:
        umbral[f, c, x] = 255

uI = imagen1.copy()
for f, c, x in np.ndindex(imagen1.shape):
#for f, c in np.ndindex(imagen1.shape):
    if imagen1[f, c, x] <= 100:
        uI[f, c, x] = 255
    elif imagen1[f, c, x] > 100:
        uI[f, c, x] = 0

p1 = 150
p2 = 220

u = imagen1.copy()
for f, c, x in np.ndindex(imagen1.shape):
#for f, c in np.ndindex(imagen1.shape):
    if p1 < imagen1[f, c, x] and imagen1[f, c, x] < p2:
        u[f, c, x] = 0
    elif imagen1[f, c, x] <= p1 or imagen1[f, c, x] >= p2:
        u[f, c, x] = 255

p1 = 50
p2 = 150

uIA = imagen1.copy()
for f, c, x in np.ndindex(imagen1.shape):
#for f, c in np.ndindex(imagen1.shape):
    if p1 < imagen1[f, c, x] and imagen1[f, c, x] < p2:
        uI[f, c, x] = 255
    elif imagen1[f, c, x] <= p1 or imagen1[f, c, x] >= p2:
        uI[f, c, x] = 0

p1 = 150
p2 = 220

uG = imagen1.copy()
for f, c, x in np.ndindex(imagen1.shape):
#for f, c in np.ndindex(imagen1.shape):
    if p1 < imagen1[f, c, x] and imagen1[f, c, x] < p2:
        uG[f, c, x] = imagen1[f, c, x]
    elif imagen1[f, c, x] <= p1 or imagen1[f, c, x] >= p2:
        uG[f, c, x] = 255

p1 = 150
p2 = 220

uGI = imagen1.copy()
for f, c, x in np.ndindex(imagen1.shape):
#for f, c in np.ndindex(imagen1.shape):
    if p1 < imagen1[f, c, x] and imagen1[f, c, x] < p2:
        uGI[f, c, x] = 255-imagen1[f, c, x]
    elif imagen1[f, c, x] <= p1 or imagen1[f, c, x] >= p2:
        uGI[f, c, x] = 255

p1 = 50
p2 = 150

extendida = imagen1.copy()
for f, c, x in np.ndindex(imagen1.shape):
#for f, c in np.ndindex(imagen1.shape):
    if p1 < imagen1[f, c, x] and imagen1[f, c, x] < p2:
        extendida[f, c, x] = (imagen1[f, c, x]-p1)*(255/(p2-p1))
    elif imagen1[f, c, x] <= p1 or imagen1[f, c, x] >= p2:
        extendida[f, c, x] = 0

p1 = 50
p2 = 150

reduccion = imagen1.copy()
for f, c, x in np.ndindex(imagen1.shape):
#for f, c in np.ndindex(imagen1.shape):
    if imagen1[f, c, x] <= 50:
        reduccion[f, c, x] = 0
    elif 50 < imagen1[f, c, x] and imagen1[f, c, x] <= 100:
        reduccion[f, c, x] = 32
    elif 100 < imagen1[f, c, x] and imagen1[f, c, x] <= 150:
        reduccion[f, c, x] = 64
    elif 150 < imagen1[f, c, x] and imagen1[f, c, x] <= 200:
        reduccion[f, c, x] = 128
    elif 200 < imagen1[f, c, x] and imagen1[f, c, x] <= 255:
        reduccion[f, c, x] = 255


cv.imwrite("a_Color.png", imagen1)
cv.imwrite("b_Color.png", inversa)
cv.imwrite("c_Color.png", umbral)
cv.imwrite("d_Color.png", uI)
cv.imwrite("e_Color.png", u)
cv.imwrite("e.1_Color.png", uIA)
cv.imwrite("f_Color.png", uG)
cv.imwrite("g_Color.png", uGI)
cv.imwrite("h_Color.png", extendida)
cv.imwrite("i_Color.png", reduccion)