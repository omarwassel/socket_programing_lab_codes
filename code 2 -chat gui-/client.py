#!/usr/bin/python3
import socket
import _thread
from  tkinter import *
from functools import *


wind=Tk()
wind.title("Client")
wind.geometry('400x300')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 12345))

msg_text_field=Text(wind,bg="white",fg="black",width=20,height=4,font=('Helvetica','15'))
msg_text_field.grid(row=0,column=0)

server_lb=Label(wind,text="Sever : ",font=('Helvetica','15'))
server_lb.grid(row=3,column=0)

btn=Button(wind,text="Send ",bg="yellow",fg="black",width=19,height=1,font=('Helvetica','15'))
btn.grid(row=2,column=0)

def send():
    msg=msg_text_field.get(1.0,END)
    s.send(bytes(msg, 'utf-8'))


def recive():
    while True:
        msg = s.recv(1024).decode('utf-8')
        server_lb["text"]="Sever : "+msg
   
btn.config(command=partial(send))

_thread.start_new_thread(recive,())


wind.mainloop()

   
    

