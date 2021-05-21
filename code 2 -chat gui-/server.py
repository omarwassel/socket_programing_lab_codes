#!/usr/bin/python3
import socket
import _thread
from  tkinter import *
from functools import *



wind=Tk()
wind.title("Server")
wind.geometry('400x300')

msg_text_field=Text(wind,bg="white",fg="black",width=20,height=4,font=('Helvetica','15'))
msg_text_field.grid(row=0,column=0)

server_lb=Label(wind,text="Client : ",font=('Helvetica','15'))
server_lb.grid(row=3,column=0)

btn=Button(wind,text="Send ",bg="blue",fg="black",width=19,height=1,font=('Helvetica','15'))
btn.grid(row=2,column=0)


def send(c):
    c.send(bytes(msg_text_field.get(1.0,END), 'utf-8'))

def recive(c):
    while True:
        msg = c.recv(1024).decode('utf-8')
        server_lb["text"]="Client : "+msg
   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 12345))
s.listen(5)
print("listening........")
c, address = s.accept()
print(f"client {address[1]} connected")

btn.config(command=partial(send,c))

_thread.start_new_thread(recive,(c,))

wind.mainloop()

   
