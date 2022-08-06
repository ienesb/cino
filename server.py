import cv2
import numpy as np

import socket
import pickle

import time

metadata = bytes("endofimg", "utf-8")
metadatalength = len(metadata)

# img = cv2.imread("lena.jpg")
# msg = pickle.dumps(img)
cap = cv2.VideoCapture(0)

IP = ""
PORT = 2516

server = socket.socket()
server.bind((IP, PORT))     #94.54.56.215 public ip
server.listen()
server.settimeout(0.1)
clients = []
while True:
    # msg = bytes(f"{len(msg):<10}", "utf-8") + msg
    
    try:
        client, addr = server.accept()
        clients.append(client)
        print(f"{addr}")
    except TimeoutError:
        pass
    except KeyboardInterrupt:
        break
    
    _, img = cap.read()
    
    msg = pickle.dumps(img)
    # msg = bytes(f"{len(msg):<10}", "utf-8") + msg
    msg = msg + metadata
    
    for c in clients:
        c.send(msg)
    time.sleep(0.05)


server.close()
cv2.destroyAllWindows()
print("done")