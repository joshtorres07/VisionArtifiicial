import cv2
imagen = cv2.imread('imagenCirculos.png')
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_,th =  cv2.threshold(grises, 240, 255, cv2.THRESH_BINARY_INV)

cnts,_ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen, cnts, -1, (255,0,0),2)
print('Contornos: ', len(cnts))#len()regresa el numero de los contornos
font = cv2.FONT_HERSHEY_SIMPLEX
numero = len(cnts)
i=0
for c in cnts:  #este ciclo permite enumerar cada contorno encontrado
  M=cv2.moments(c)
  if (M["m00"]==0): M["m00"]=1
  x=int(M["m10"]/M["m00"])
  y=int(M['m01']/M['m00'])
  mensaje = 'Num :' + str(i+1)
  cv2.putText(imagen,mensaje,(x-40,y),font,0.75,
    (255,0,0),2,cv2.LINE_AA)
  cv2.drawContours(imagen, [c], 0, (255,0,0),2)
  cv2.imshow('Imagen', imagen)
  cv2.waitKey(0)
  i = i+1
cv2.putText(imagen,"Contornos " + str(numero),(x-200,y-20),font,0.75,
    (255,0,0),2,cv2.LINE_AA)
cv2.imwrite("imagenNuevaCirculos.png",imagen)
cv2.destroyAllWindows()