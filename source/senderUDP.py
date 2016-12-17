#!/usr/bin/env python

import socket


UDP_IP = '127.0.0.1'
UDP_PORT = 1025
BUFFER_SIZE = 1024
MESSAGE = "whats my next calendar event"

print("sending data:", MESSAGE)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.connect((UDP_IP, UDP_PORT))
s.sendto((bytes(MESSAGE, 'UTF-8')), (UDP_IP, UDP_PORT))

s1.bind((UDP_IP, UDP_PORT))
print("OK")
while True:

    data, addr = s.recvfrom(BUFFER_SIZE) # buffer size is 1024 bytes
    print("received message:", data)

s.close()
