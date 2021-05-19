from tkinter import *
from tkinter import messagebox
from functools import *
import socket
import _thread
# 1 -> X
# 2 -> O
vals = [0 for i in range(9)]
count = 0
s = socket.socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 12345))
s.listen(5)
c, address = s.accept()
print(f"client {c} connected")
flag = 1
def listen(c):
    global flag
    while True:
        msg = int(c.recv(1024).decode('utf-8'))
        print(msg)
        flag = 0
        play(btn=btns[msg], index=msg)
        check()
        
    
_thread.start_new_thread(listen, (c,))
def check():
    global count
    if(vals[0] == vals[1] == vals[2] != 0):
        if(turn == 'x'):
            messagebox.showinfo('', message='O wins')
        else:
            messagebox.showinfo('', message='X wins')
    elif(vals[3] == vals[4] == vals[5] != 0):
        if(turn == 'x'):
            messagebox.showinfo('', message='O wins')
        else:
            messagebox.showinfo('', message='X wins')
    elif(vals[6] == vals[7] == vals[8] != 0):
        if(turn == 'x'):
            messagebox.showinfo('', message='O wins')
        else:
            messagebox.showinfo('', message='X wins')
    elif(vals[0] == vals[3] == vals[6] != 0):
        if(turn == 'x'):
            messagebox.showinfo('', message='O wins')
        else:
            messagebox.showinfo('', message='X wins')
    elif(vals[1] == vals[4] == vals[7] != 0):
        if(turn == 'x'):
            messagebox.showinfo('', message='O wins')
        else:
            messagebox.showinfo('', message='X wins')
    elif(vals[2] == vals[5] == vals[8] != 0):
        if(turn == 'x'):
            messagebox.showinfo('', message='O wins')
        else:
            messagebox.showinfo('', message='X wins')
    elif(vals[0] == vals[4] == vals[8] != 0):
        if(turn == 'x'):
            messagebox.showinfo('', message='O wins')
        else:
            messagebox.showinfo('', message='X wins')
    elif(vals[2] == vals[4] == vals[6] != 0):
        if(turn == 'x'):
            messagebox.showinfo('', message='O wins')
        else:
            messagebox.showinfo('', message='X wins')
    elif(count == 9):
        messagebox.showinfo('', message='DRAW')


def play(btn, index):
    global turn,count, flag
    if(vals[index] != 0):
        return
    if(flag == 2):
        return
    if(turn == 'x'):
        btn.config(text='X')
        vals[index] = 1
        turn = 'o'
    else:
        btn.config(text='O')
        turn = 'x'
        vals[index] = 2
        return
    count += 1
    flag += 1
    c.send(bytes(str(index), 'utf-8'))
    

    



app = Tk()
turn = 'x'
app.geometry("700x500")
app.title("p1")
# labelx = Label(app, text="player1 : X")
# labely = Label(app, text="player1 : O")
# labelx.grid(column=0, row=0)
# labely.grid(column=0, row=1)
btn1 = Button(app, text=' ', width=5, height=5)
btn1.config(command=partial(play, btn1, 0))
btn1.grid(column=0, row=0)
btn2 = Button(app, text=' ', width=5, height=5)
btn2.config(command=partial(play, btn2, 1))
btn2.grid(column=0, row=1)
btn3 = Button(app, text=' ', width=5, height=5)
btn3.config(command=partial(play, btn3, 2))
btn3.grid(column=0, row=2)
btn4 = Button(app, text=' ', width=5, height=5)
btn4.config(command=partial(play, btn4, 3))
btn4.grid(column=1, row=0)
btn5 = Button(app, text=' ', width=5, height=5)
btn5.config(command=partial(play, btn5, 4))
btn5.grid(column=1, row=1)
btn6 = Button(app, text=' ', width=5, height=5)
btn6.config(command=partial(play, btn6, 5))
btn6.grid(column=1, row=2)
btn7 = Button(app, text=' ', width=5, height=5)
btn7.config(command=partial(play, btn7, 6))
btn7.grid(column=2, row=0)
btn8 = Button(app, text=' ', width=5, height=5)
btn8.config(command=partial(play, btn8, 7))
btn8.grid(column=2, row=1)
btn9 = Button(app, text=' ', width=5, height=5)
btn9.config(command=partial(play, btn9, 8))
btn9.grid(column=2, row=2)
btns = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
app.mainloop()
