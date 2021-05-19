#!/usr/bin/python3
import socket
import signal
import sys
import _thread


def signal_handler(sig, frame):
    global s
    print("Closing the socket")
    s.close()

    sys.exit(0)


def listen(s):
    while True:
        msg = s.recv(1024)
        print()
        print(msg.decode('utf-8'))

def talk(s):
    while True:
        msg = input()
        s.send(bytes(msg, 'utf-8'))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
signal.signal(signal.SIGINT, signal_handler)
s.connect(('127.0.0.1', 12345))
_thread.start_new_thread(listen, (s,))
_thread.start_new_thread(talk, (s,))

while(1):
    pass
