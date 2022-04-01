import cv2

gray = cv2.imread("sdf.jpg",0)
cv2.namedWindow("Umbralizacion")

def actualiza(umbral):
    t,img =cv2.threshold(gray,umbral,255,cv2.THRESH_BINARY)
    cv2.imshow("Umbralizacion",img)

cv2.createTrackbar("Umbral","Umbralizacion",0,255,actualiza)
actualiza(0)
cv2.waitKey(0)
cv2.destroyAllWindows()