#JOSUE DANIEL TORRES SANTOS
#VISION ARTIFICIAL
#23/05/23


import cv2 as cv
cap = cv.VideoCapture("changuito.mp4")
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))

fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('Video Generado.mp4', fourcc, 40, (width, height), isColor=True)
while True:
    ret, frame = cap.read()
    if ret == True:
        nF = cv.medianBlur(frame, 17)
        cv.imshow("Video", nF)
        out.write(nF)
        if cv.waitKey(1)&0xFF == ord('z'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows