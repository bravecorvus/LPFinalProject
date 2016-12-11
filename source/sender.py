#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 1026
BUFFER_SIZE = 1024
MESSAGE = "append1([a,b], c, X)."

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(bytes(MESSAGE, 'UTF-8'))

sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)