import cv2 as cv
import numpy as np
import os

imagen = cv.imread("knyColores.png")
hsv = cv.cvtColor(imagen, cv.COLOR_BGR2HSV)

rojoBajo = np.array([170, 100, 100], np.uint8)  # 170, 100, 100
rojoAlto = np.array([180, 255, 255], np.uint8)  # 180, 255, 255

verdeBajo = np.array([35, 100, 100], np.uint8)  # 35, 100, 100
verdeAlto = np.array([77, 255, 255], np.uint8)  # 77, 255, 255

azulBajo = np.array([100, 100, 100], np.uint8)  # 110, 100, 100
azulAlto = np.array([135, 255, 255], np.uint8)  # 130, 255, 255

amarilloBajo = np.array([20, 100, 100], np.uint8)  # 20, 100, 100
amarilloAlto = np.array([35, 255, 255], np.uint8)  # 35, 255, 255

naranjaBajo = np.array([5, 100, 100], np.uint8)  # 5, 100, 100
naranjaAlto = np.array([15, 255, 255], np.uint8)  # 15, 255, 255

moradoBajo = np.array([125, 100, 100], np.uint8)  # 125, 100, 100
moradoAlto = np.array([155, 255, 255], np.uint8)  # 155, 255, 255

rosaBajo = np.array([160, 100, 100], np.uint8)  # 160, 100, 100
rosaAlto = np.array([170, 255, 255], np.uint8)  # 170, 255, 255

blancoBajo = np.array([0, 0, 200], np.uint8)  # 0, 0, 200
blancoAlto = np.array([180, 50, 255], np.uint8)  # 180, 50, 255

maskred = cv.inRange(hsv, rojoBajo, rojoAlto)
maskgreen = cv.inRange(hsv, verdeBajo, verdeAlto)
maskblue = cv.inRange(hsv, azulBajo, azulAlto)
maskyellow = cv.inRange(hsv, amarilloBajo, amarilloAlto)
maskorange = cv.inRange(hsv, naranjaBajo, naranjaAlto)
maskpurple = cv.inRange(hsv, moradoBajo, moradoAlto)
maskpink = cv.inRange(hsv, rosaBajo, rosaAlto)
maskwhite = cv.inRange(hsv, blancoBajo, blancoAlto)

maskresult = cv.bitwise_or(maskred, maskgreen)
maskresult = cv.bitwise_or(maskresult, maskblue)
maskresult = cv.bitwise_or(maskresult, maskyellow)
maskresult = cv.bitwise_or(maskresult, maskorange)
maskresult = cv.bitwise_or(maskresult, maskpurple)
maskresult = cv.bitwise_or(maskresult, maskpink)
maskresult = cv.bitwise_or(maskresult, maskwhite)

result = cv.bitwise_and(imagen, imagen, mask=maskresult)

cv.imwrite("colores.png", result)
cv.imshow('Colores Imagen', result)
cv.waitKey(0)
cv.destroyAllWindows()
