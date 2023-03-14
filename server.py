import cv2
import numpy as np

import socket
import pickle

import time

metadata = bytes("endofimg", "utf-8")
metadatalength = len(metadata)

# cap = cv2.VideoCapture(0)
img = cv2.imread("lena.jpg")

IP = ""
PORT = 8000

server = socket.socket()
server.bind((IP, PORT))     #94.54.56.215 public ip
server.listen()
server.settimeout(0.1)
clients = []
while True:
    
    try:
        client, addr = server.accept()
        clients.append(client)
        print(f"{addr}")
    except TimeoutError:
        pass
    except KeyboardInterrupt:
        break

    if len(clients) > 0:
        # cap.release()
        # cap = cv2.VideoCapture(0)
        # _, img = cap.read()
        
        msg = pickle.dumps(img)
        msg = msg + metadata
        
        for c in clients:
            try:
                c.send(msg)
            except BrokenPipeError:
                clients.remove(c)
        time.sleep(0.05)
    else:
        pass
        # cap.release()

server.close()
# cap.release()
cv2.destroyAllWindows()
print("done")