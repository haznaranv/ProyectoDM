import SimpleHTTPServer
import cv2
import threading
import socketserver

# Inicializa el objeto VideoCapture con la cámara web por defecto
cap = cv2.VideoCapture(0)

# Configura el ancho y alto del frame a transmitir
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# Inicializa el codec y crea el objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter('http://192.168.1.47:8080/live/stream', fourcc, 20.0, (320, 240))

# Clase para manejar las solicitudes HTTP
class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/live/stream':
            self.send_response(200)
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=frame')
            self.end_headers()
            while True:
                # Lee el siguiente frame de la cámara
                ret, frame = cap.read()
                if not ret:
                    break

                # Escribir el frame a la salida
                out.write(frame)

                # Enviar el frame al cliente
                self.wfile.write("--frame\r\n")
                self.send_header('Content-Type', 'image/jpeg')
                self.send_header('Content-Length', len(frame))
                self.end_headers()
                self.wfile.write(frame)
                self.wfile.write("\r\n")

# Inicia el servidor HTTP
httpd = socketserver.TCPServer (("", 8080), Handler)
httpd.serve_forever()
