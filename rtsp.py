import cv2
import threading




# Inicializa el objeto VideoCapture con la cámara web por defecto
cap = cv2.VideoCapture(0)

# Configura el ancho y alto del frame a transmitir
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Inicializa el codec y crea el objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'MjPG')
out = cv2.VideoWriter('http://localhost:8080/live/stream', fourcc, 20.0, (640, 480))  #cambie el rtsp por el http

while True:
    # Lee el siguiente frame de la cámara
    ret, frame = cap.read()
    if not ret:
        break

    # Escribir el frame a la salida
    out.write(frame)

    # Mostrar el frame en una ventana
    cv2.imshow('Live Stream', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
out.release()
cv2.destroyAllWindows()
