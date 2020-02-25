from tkinter import *

meshal=Tk()
meshal.geometry("200x200")


meshal.title('nothing')


def sum():

    num=int(input('Enter first number: '))
    num2=int(input('Enter second number: '))
    print('The sum is :',num2+num)

def sub():
    num = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    print('The sub is :', num- num2)

def mult():
    num = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    print('The mult is :', num2 * num)

def div():
    num = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    print('The div is :', num2 /num)

frame2 = Frame(meshal, highlightbackground="black",bg="#F9ECE9", highlightthickness=3, width=330, height=150)
frame2.place(x=370,y=180)
try:
 a=Button(meshal,text="Enter here to sum",fg='black',bg='#4dc3ff',width='15',height='2',cursor="dotbox",bd="3px",activebackground="#cccc00",command=sum)
 a.place(x=400,y=200)
 b=Button(meshal,text="Enter here to sub",fg='black',bg='#4dc3ff',width='15',height='2',cursor="dotbox",bd="3px",activebackground="#cccc00",command=sub)
 b.place(x=400,y=250)

 c=Button(meshal,text="Enter here to mult",fg='black',bg='#4dc3ff',width='15',height='2',cursor="dotbox",bd="3px",activebackground="#cccc00",command=mult)
 c.place(x=550,y=200)
 d=Button(meshal,text="Enter here to div",fg='black',bg='#4dc3ff',width='15',height='2',cursor="dotbox",bd="3px",activebackground="#cccc00",command=div)
 d.place(x=550,y=250)
except TypeError:
    print("There is some Error")




meshal.mainloop()






