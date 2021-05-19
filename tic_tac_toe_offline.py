from  tkinter import *
from  tkinter import messagebox


window=Tk()
window.title("Tic Tac Toe")
window.geometry('400x300')


lb1=Label(window,text="Player_1 : X",font=('Helvetica','15'))
lb1.grid(row=0,column=0)

lb2=Label(window,text="Player_2 : O",font=('Helvetica','15'))
lb2.grid(row=1,column=0)

def win (char):
    messagebox.showinfo("Congratulations",char)
    window.destroy()

def check_equal(x,y,z):
    global list
    if x["text"]==y["text"] and y["text"]==z["text"]:
        if x["text"]=="O" or x["text"] =="X":
           return True
    return False

cnt=1
def check():
    global cnt

    if check_equal(bt1,bt2,bt3):
         win(bt1["text"])
    elif check_equal(bt4,bt5,bt6):
         win(bt4["text"])
    elif check_equal(bt7,bt8,bt9):
         win(bt7["text"])

    elif check_equal(bt1,bt4,bt7):
         win(bt1["text"])
    elif check_equal(bt2,bt5,bt8):
         win(bt2["text"])
    elif check_equal(bt3,bt6,bt9):
         win(bt3["text"])

    elif check_equal(bt1,bt5,bt9):
         win(bt1["text"])
    elif check_equal(bt3,bt5,bt7):
         win(bt3["text"])
    
    cnt+=1
    if cnt==10:
         messagebox.showinfo("Game Over")
         window.destroy()



turn = 1

def clicked1():
    global turn
    if bt1["text"]==" ":
        if turn == 1:
            bt1["text"]="O"
            turn=2
        else:
            bt1["text"]="X"
            turn=1
        check()

def clicked2():
    global turn
    if bt2["text"]==" ":
        if turn == 1:
            bt2["text"]="O"
            turn=2
        else:
            bt2["text"]="X"
            turn=1
        check()

def clicked3():
    global turn
    if bt3["text"]==" ":
        if turn == 1:
            bt3["text"]="O"
            turn=2
        else:
            bt3["text"]="X"
            turn=1
        check()

def clicked4():
    global turn
    if bt4["text"]==" ":
        if turn == 1:
            bt4["text"]="O"
            turn=2
        else:
            bt4["text"]="X"
            turn=1
        check()

def clicked5():
    global turn
    if bt5["text"]==" ":
        if turn == 1:
            bt5["text"]="O"
            turn=2
        else:
            bt5["text"]="X"
            turn=1
        check()

def clicked6():
    global turn
    if bt6["text"]==" ":
        if turn == 1:
            bt6["text"]="O"
            turn=2
        else:
            bt6["text"]="X"
            turn=1
        check()

def clicked7():
    global turn
    if bt7["text"]==" ":
        if turn == 1:
            bt7["text"]="O"
            turn=2
        else:
            bt7["text"]="X"
            turn=1
        check()

def clicked8():
    global turn
    if bt8["text"]==" ":
        if turn == 1:
            bt8["text"]="O"
            turn=2
        else:
            bt8["text"]="X"
            turn=1
        check()

def clicked9():
    global turn
    if bt9["text"]==" ":
        if turn == 1:
            bt9["text"]="O"
            turn=2
        else:
            bt9["text"]="X"
            turn=1
        check()
 

bt1=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','10'),command=clicked1)
bt1.grid(row=0,column=1)

bt2=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','10'),command=clicked2)
bt2.grid(row=0,column=2)

bt3=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','10'),command=clicked3)
bt3.grid(row=0,column=3)

bt4=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','10'),command=clicked4)
bt4.grid(row=1,column=1)

bt5=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','10'),command=clicked5)
bt5.grid(row=1,column=2)

bt6=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','10'),command=clicked6)
bt6.grid(row=1,column=3)

bt7=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','10'),command=clicked7)
bt7.grid(row=2,column=1)

bt8=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','10'),command=clicked8)
bt8.grid(row=2,column=2)

bt9=Button(window,text=" ",bg="yellow",fg="black",width=3,height=1,font=('Helvetica','10'),command=clicked9)
bt9.grid(row=2,column=3)

window.mainloop()