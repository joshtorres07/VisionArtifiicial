import cv2
import numpy as np

gray = cv2.imread("sdf.jpg",0)
h,w = gray.shape

binary = np.ndarray((h,w),np.uint8)
binaryInverse = np.ndarray((h,w),np.uint8)
umbralGray = binary.copy()
umbralGrayInv = umbralGray.copy()
umbralExt = binary.copy()
red1 = binary.copy()
red2 = red1.copy()
nueva = red1.copy()
imax = gray.max
imin = gray.min
umbral = 100
umbral2 = 150

for i in range(h):
    for j in range(w):
        negative = 255 - gray[i,j]
        negativo = 0
        inverse = 255
        if umbral <= gray[i,j]:
            binary[i,j] = negativo
            binaryInverse[i,j] = inverse
        else:
            binary[i,j] =inverse
            binaryInverse[i,j] = negativo
        if (gray[i,j]<umbral):
            umbralGray[i,j] = inverse
        else:
            umbralGray[i,j] =  gray[i,j]

        #umbral gris invertido
        if(gray[i,j] <= umbral or gray[i,j]>=umbral2):
            umbralGrayInv[i,j] = 255
        elif(umbral < gray[i,j] <umbral2):
            umbralGrayInv[i,j]= negative

        #extension
        if(gray[i,j]<+ umbral or gray[i,j]>=umbral2):
            umbralExt[i,j] = 0
        elif(umbral < gray[i,j] < umbral2):
            umbralExt[i,j] = ((gray[i,j]- umbral)*(255-(umbral2 - umbral)))

        #reduccion1
        if gray[i,j] < 50:
            red1 = 0
        elif 50 < gray[i,j] < 100:
            red1 = 50
        elif 100 < gray[i,j] < 150:
            red1 = 100
        elif 150 < gray[i,j] < 200:
            red1 = 150
        elif 200 < gray[i,j] < 250:
            red1 = 200
        elif 250 < gray[i,j]:
            red1 = 255

        red2[i,j] = (umbral2 -umbral)/(imax-imin)*(gray[i,j]-imin)+ umbral

        nueva[i,j] = (red2[i,j-umbral])/(umbral2-umbral)*(imax-imin)+imin

cv2.imshow("binaria", binary)
cv2.imshow("Binaria Inversa",binaryInverse)
cv2.imshow("Gris", umbralGray)
cv2.imshow("Gris invertido", umbralGrayInv)
cv2.imshow("Extension",umbralExt)
cv2.imshow("Reduccion 1",red1)
cv2.imshow("Reduccion 2",red2)
cv2.imshow("Nueva", nueva)
cv2.waitKey(0)
cv2.destroyAllWindows()

