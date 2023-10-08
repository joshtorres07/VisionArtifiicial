#JOSUE DANIEL TORRES SANTOS
#ACTIVIDAD 6: UMBRALIZACION
#23/05/23
#VISION ARTIFICIAL

import cv2
import numpy as np

file = "tanjiro.jpg"
img = cv2.imread(file,1)
h,w,c = img.shape
for i in range (h):
    for j in range (w):
        b,g,r = img[i,j]
        img[i,j] = [255-b, 255-g, 255-r]
cv2.imshow("Invertida",img)
cv2.imwrite("Invertida.jpg", img)

img = cv2.imread(file,1)
h,w,c = img.shape
t,umbral = cv2.threshold(img,100,255, cv2.THRESH_BINARY)
cv2.imshow("Umbral",umbral)
cv2.imwrite("Umbral.jpg",umbral)

img = cv2.imread(file,1)
h,w,c = img.shape
t,uI = cv2.threshold(img,100,255, cv2.THRESH_BINARY_INV)
cv2.imshow("umbralInvertido",uI)
cv2.imwrite("umbralInvertido.jpg",uI)

img = cv2.imread(file,1)
h,w,c = img.shape
t,uB = cv2.threshold(img,150,220, cv2.THRESH_BINARY)
cv2.imshow("UmbralBinario",uB)
cv2.imwrite("UmbralBinario.jpg",uB)


img = cv2.imread(file,1)
h,w,c = img.shape
t,uBI = cv2.threshold(img,50,150,
cv2.THRESH_BINARY_INV)
cv2.imshow("UmbralBinarioInvertido",uBI)
cv2.imwrite("UmbralBinarioInvertido.jpg",uBI)

img = cv2.imread(file,0)
t,uG = cv2.threshold(img,150,220, cv2.THRESH_BINARY)
cv2.imshow("Grises ",uG)
cv2.imwrite("Grises.jpg",uG)

img = cv2.imread(file,0)
t,uBI = cv2.threshold(img,150,220, cv2.THRESH_BINARY_INV)
cv2.imshow("GrisesInvertidos",uBI)
cv2.imwrite("GriesesInvertidos.jpg",uBI)

img = cv2.imread(file,0)
t,extension = cv2.threshold(img,50,150, cv2.THRESH_TRIANGLE)
cv2.imshow("Extension",extension)
cv2.imwrite("Extension.jpg",extension)

mg = cv2.imread(file,0)
h,w=img.shape
p1=50
p2=100
p3=150
p4=200
q1=32
q2=64
q3=128
q4=255
for i in range(h):
    for j in range(w):
        if img[i,j] <p1:
            img[i,j] = 0
        elif img[i,j] <= p1 and img[i,j] < p2:
            img[i,j] = q1
        elif img[i,j] <= p2 and img[i,j] < p3:
            img[i,j] = q2
        elif img[i,j] <= p3 and img[i,j] < p4:
            img[i,j] = q3
        elif img[i,j] <= p4 and img[i,j]<250:
            img[i,j] = q4
        elif img[i,j]<=250:
            img[i,j] = 255
cv2.imshow("Reduccion",img)
cv2.imwrite("Reduccion.jpg",img)

cv2.waitKey(0)
cv2.destroyAllWindows()