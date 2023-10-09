import cv2 as cv
import numpy as np

cap = cv.VideoCapture("semestre sueltame.mp4")
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))

fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('Video Generado.mp4', fourcc, 40, (width, height), isColor=True)

rojoBajo = np.array([160, 100, 100], np.uint8)
rojoAlto = np.array([180, 255, 255], np.uint8)

verdeBajo = np.array([35, 100, 100], np.uint8)
verdeAlto = np.array([77, 255, 255], np.uint8)

azulBajo = np.array([100, 100, 100], np.uint8)
azulAlto = np.array([135, 255, 255], np.uint8)

amarilloBajo = np.array([20, 100, 100], np.uint8)
amarilloAlto = np.array([35, 255, 255], np.uint8)

naranjaBajo = np.array([5, 100, 100], np.uint8)
naranjaAlto = np.array([15, 255, 255], np.uint8)

moradoBajo = np.array([125, 100, 100], np.uint8)
moradoAlto = np.array([155, 255, 255], np.uint8)

rosaBajo = np.array([160, 100, 100], np.uint8)
rosaAlto = np.array([170, 255, 255], np.uint8)

blancoBajo = np.array([0, 0, 200], np.uint8)
blancoAlto = np.array([180, 50, 255], np.uint8)

cafeBajo = np.array([10, 50, 50], np.uint8)  # Rango bajo para el color café
cafeAlto = np.array([20, 255, 255], np.uint8)  # Rango alto para el color café

while True:
    ret, imagen = cap.read()
    if ret == True:
        hsv = cv.cvtColor(imagen, cv.COLOR_BGR2HSV)

        maskred = cv.inRange(hsv, rojoBajo, rojoAlto)
        maskgreen = cv.inRange(hsv, verdeBajo, verdeAlto)
        maskblue = cv.inRange(hsv, azulBajo, azulAlto)
        maskyellow = cv.inRange(hsv, amarilloBajo, amarilloAlto)
        maskorange = cv.inRange(hsv, naranjaBajo, naranjaAlto)
        maskpurple = cv.inRange(hsv, moradoBajo, moradoAlto)
        maskpink = cv.inRange(hsv, rosaBajo, rosaAlto)
        maskwhite = cv.inRange(hsv, blancoBajo, blancoAlto)
        maskcafe = cv.inRange(hsv, cafeBajo, cafeAlto)

        maskresult = cv.bitwise_or(maskred, maskgreen)
        maskresult = cv.bitwise_or(maskresult, maskblue)
        maskresult = cv.bitwise_or(maskresult, maskyellow)
        maskresult = cv.bitwise_or(maskresult, maskorange)
        maskresult = cv.bitwise_or(maskresult, maskpurple)
        maskresult = cv.bitwise_or(maskresult, maskpink)
        maskresult = cv.bitwise_or(maskresult, maskwhite)
        maskresult = cv.bitwise_or(maskresult, maskcafe)

        result = cv.bitwise_and(imagen, imagen, mask=maskresult)

        cv.imshow("Video", result)
        out.write(result)
        if cv.waitKey(1) & 0xFF == ord('z'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()
