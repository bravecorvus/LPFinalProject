#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 1026
BUFFER_SIZE = 1024
MESSAGE = "how are you"

print("sending data:", MESSAGE)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(bytes(MESSAGE, 'UTF-8'))
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)