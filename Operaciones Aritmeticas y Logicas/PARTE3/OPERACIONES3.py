#JOSUE DANIEL TORRES SANTOS
#VISION ARTIFICIAL
#23/05/23
#ACTIVIDAD 3 UNIDAD 2

import cv2

# Crear una función para aplicar la máscara al video en streaming
def aplicar_mascara(video_path, mascara_path):
    # Cargar el video en streaming
    video_stream = cv2.VideoCapture(video_path)

    # Obtener la información de los frames del video
    fps = video_stream.get(cv2.CAP_PROP_FPS)
    width = int(video_stream.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_stream.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Crear el objeto VideoWriter para guardar el video resultante
    video_salida = cv2.VideoWriter('resultado.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # Cargar la máscara
    mascara = cv2.imread(mascara_path)

    while True:
        # Leer un frame del video
        ret, frame = video_stream.read()

        if not ret:
            break

        # Redimensionar la máscara para que tenga las mismas dimensiones que el frame
        mascara = cv2.resize(mascara, (frame.shape[1], frame.shape[0]))

        # Aplicar la máscara utilizando una operación lógica AND
        resultado = cv2.bitwise_and(frame, mascara)

        # Mostrar el video con la máscara aplicada
        cv2.imshow("Video con máscara", resultado)

        # Guardar el frame con la máscara aplicada en el video de salida
        video_salida.write(resultado)

        # Detener la ejecución si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar los recursos
    video_stream.release()
    video_salida.release()
    cv2.destroyAllWindows()

# Llamar a la función para aplicar la máscara al video en streaming
aplicar_mascara('capybaras.mp4', 'aphelios.png')
