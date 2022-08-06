import cv2
import numpy as np

import socket
import pickle

import sys

metadata = bytes("endofimg", "utf-8")
metadatalength = len(metadata)

IP = "6.tcp.eu.ngrok.io"
PORT = 14620

# IP = "127.0.0.1"
# PORT = 2516

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((IP,PORT))

fullmsg = b""
while True:
    
    while True:
        msg = s.recv(1024*500)    
        fullmsg += msg
        if metadata in fullmsg:
            break
        
        # if len(fullmsg[10:]) >= msglen:
        #     print("**********")
        #     with open("data.txt", "w") as f:
        #         f.write(str(fullmsg))
        #     # print(fullmsg)
        #     print("**********")
        #     sys.exit()
        #     break
    
    img = pickle.loads(fullmsg[:fullmsg.find(metadata)])
    fullmsg = fullmsg[fullmsg.find(metadata) + metadatalength:]
    cv2.imshow("frame", img)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cv2.destroyAllWindows()
s.close()