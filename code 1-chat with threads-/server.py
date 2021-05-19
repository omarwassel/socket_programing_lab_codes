#!/usr/bin/python3
import socket
import sys
import _thread

clients = []


def listen(c):
    while True:
        msg = c.recv(1024).decode('utf-8')
        for c in clients:
            c.send(bytes(msg, 'utf-8'))



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 12345))
s.listen(5)


while(1):
    c, address = s.accept()
    print(f"client {c} connected")
    clients.append(c)
    _thread.start_new_thread(listen, (c,))
