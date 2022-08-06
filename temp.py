import cv2
import numpy as np

import socket
import pickle

# img1 = cv2.imread("lena.jpg")
# img2 = cv2.imread("gollum.png")

# data1 = pickle.dumps(img1)
# data2 = pickle.dumps(img2)

# data = data1 + bytes("endofimg", "utf-8") + data2

# img1data = data[:data.find(bytes("endofimg", "utf-8"))]
# img2data = data[data.find(bytes("endofimg", "utf-8")) + 8:]

# receivedimg1 = pickle.loads(img1data)
# receivedimg2 = pickle.loads(img2data)


# cv2.imshow("window1", receivedimg1)
# cv2.imshow("window2", receivedimg2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# s = "qwsdertadyuioasdhsdjkghdasdzmc"

# print(s.find("asd"))
# print(s[:s.find("asd")])
# print(s[s.find("asd")+3:])


metadata = bytes("endofimg", "utf-8")
print(metadata)
print(len(metadata))
