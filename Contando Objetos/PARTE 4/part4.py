import cv2
import numpy as np

def drawContour(contornos, color):
  for (i,c) in enumerate(contornos):
    M = cv2.moments(c)
    if M["m00"] == 0:M["m00"] = 1
    x = int(M["m10"]/M["m00"])
    y = int(M["m01"]/M["m00"])
    cv2.drawContours(imagen, [c], 0, color, 2)
    cv2.putText(imagen, str(i+1), (x-10,y+10), 1, 2,(0,0,0),2)
imagen = cv2.imread("colores.jpg")

imgHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

rojoBajo1=np.array([0,100,20],np.uint8)
rojoAlto1=np.array([8,255,255],np.uint8)
rojoBajo2=np.array([175,100,20],np.uint8)
rojoAlto2=np.array([179,255,255],np.uint8)

verdeBajo=np.array([35,52,72],np.uint8)
verdeAlto=np.array([102,255,255],np.uint8)

amarilloBajo = np.array([20, 100, 20], np.uint8)
amarilloAlto = np.array([32, 255, 255], np.uint8)

moradoBajo=np.array([145,52,72],np.uint8)
moradoAlto=np.array([160,255,255],np.uint8)

rosaBajo=np.array([162,52,72],np.uint8)
rosaALto=np.array([170,255,255],np.uint8)

grisBajo=np.array([0,0,120],np.uint8)
grisAlto=np.array([10,100,130],np.uint8)

maskRed1=cv2.inRange(imgHSV,rojoBajo1,rojoAlto1)
maskRed2=cv2.inRange(imgHSV,rojoBajo2,rojoAlto2)
maskRed=cv2.add(maskRed1,maskRed2)
contornoRojo=cv2.findContours(maskRed,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

maskGreen=cv2.inRange(imgHSV, verdeBajo, verdeAlto)
contornoVerde=cv2.findContours(maskGreen,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

maskYellow = cv2.inRange(imgHSV, amarilloBajo, amarilloAlto)
contornoAmarillo = cv2.findContours(maskYellow, cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)[0]

maskViolet=cv2.inRange(imgHSV, moradoBajo, moradoAlto)
contornoMorado=cv2.findContours(maskViolet,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

maskPink=cv2.inRange(imgHSV, rosaBajo, rosaALto)
contornoRosa=cv2.findContours(maskPink,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

maskGray=cv2.inRange(imgHSV, grisBajo, grisAlto)
contornoGris=cv2.findContours(maskGray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

drawContour(contornoRojo, (0,255,0))
drawContour(contornoVerde, (255,255,0))
drawContour(contornoAmarillo, (0,255,255))
drawContour(contornoMorado, (255,25,0))
drawContour(contornoRosa, (125,25,20))
drawContour(contornoGris, (255,0,255))

totalContornos = len(contornoRojo+contornoVerde+contornoAmarillo+contornoMorado+contornoRosa+contornoGris)
cv2.putText(imagen,"Total de contornos: "+ str(totalContornos),(55,20), 1,2,(0,0,0),2)


cv2.putText(imagen,"Total contornos ",(55,20), 1, 2,(0,0,0),2)
cv2.imshow('Imagen', imagen)
cv2.imwrite('conteo.png', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()