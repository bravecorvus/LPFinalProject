#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 1025
BUFFER_SIZE = 1024
MESSAGE = "append1([a,b], c, X)."

print("sending data: ")
print(MESSAGE)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(bytes(MESSAGE).encode('utf-8'))
data = s.recv(BUFFER_SIZE)
s.close()

print("received data: ")
print(data)