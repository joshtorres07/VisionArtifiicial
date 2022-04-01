import cv2
from cv2 import IMREAD_COLOR
#im = cv2.imread("sdf.jpg")
#cv2.imshow("Imagen 1", im)
im2 = cv2.imread("sdf.jpg", 0)

im3 = cv2.imread("sdf.jpg",  cv2.IMREAD_COLOR)
print("shape de im", im2.shape)

print("shape de im", im3.shape)
"""im4 = cv2.imread("sdf.jpg",  cv2.IMREAD_GRAYSCALE)
cv2.imshow("Imagen 4", im4)"""
im5 = cv2.imread("sdf.jpg",  cv2.IMREAD_UNCHANGED)
cv2.imshow("Imagen 4", im5)
print("shape de im", im5.shape)
print("Size im2", im2.size)
print("Size im3", im3.size)
print("Size im5", im5.size)
print("tipos: im2 {} im3 {} im5 {}".format(im2.dtype, im3.dtype, im5.dtype))
"""print(im2)
print(im3)
print(im5)"""
color1 = im2[100][100]
print(color1)
color2 = im2.item(100,100)
print(color2)
im2[100][100] = 255
im2.itemset((100,101),255)
im2[0:100, 100:200] = 255
partelm  = im2[400:1000,400:1000]
cv2.imshow("Imagen 2 escala de gris", partelm)
b,g,r = im3[100,100]
print("azul {} verde {} rojo {}".format(b,g,r))
color3 = im3[100,100]
print(color3)
r1 = im3[100,100,0]
g1 = im3[100,100,1]
b1 = im3[100,100,2]
print("azul {} verde {} rojo {}".format(b1,g1,r1))
r2 = im3.item(100,100,0)
g2 = im3.item(100,100,1)
b2 = im3.item(100,100,2)
print("azul {} verde {} rojo {}".format(b2,g2,r2))
im3[100][100] = (255,255,225)
im3[100][100] = (255,255,225)
im3.itemset((100,10,0),255)
im3.itemset((100,10,1),255)
im3.itemset((100,10,2),255)
im3[100,102,0] = 225
im3[100,102,1] = 225
im3[100,102,2] = 225
im3[100:200,100:200,0] = 220
im3[100:200,100:200,1] = 120
im3[100:200,100:200,2] = 32
#o tambien
im3[100:200, 201:300] = [30,40,140]

azul, verde, rojo = cv2.split(im3)
cv2.imshow("azul", azul)
cv2.imshow("verde", verde)
cv2.imshow("rojo", rojo)
cv2.imshow("Imagen 3", im3)
unir = cv2.merge((verde,azul,rojo))
cv2.imwrite("zegui.jpg", unir)
cv2.imshow("rojo, azul, verde", unir)
cv2.waitKey(0)