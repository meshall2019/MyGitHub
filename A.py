import tkinter

meshal=tkinter.Tk()


meshal.title('nothing')


def sum():

    num=int(input('Enter first number: '))
    num2=int(input('Enter second number: '))
    print('The sum is :',num2+num)

def sub():
    num = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print('The sub is :', num- num2)

def mult():
    num = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print('The mult is :', num2 * num)

def div():
    num = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print('The div is :', num2 /num)


a=tkinter.Button(meshal,text="Enter here to sum",fg='black',bg='#4dc3ff',width='15',height='2', command=sum)# pady and padx other atributes
a.pack()
print("  ")
b=tkinter.Button(meshal,text="Enter here to sub",fg='black',bg='#4dc3ff',width='15',height='2',command=sub)
b.pack()
c=tkinter.Button(meshal,text="Enter here to mult",fg='black',bg='#4dc3ff',width='15',height='2',command=mult)
c.pack()
d=tkinter.Button(meshal,text="Enter here to div",fg='black',bg='#4dc3ff',width='15',height='2',command=div)
d.pack()

b.mainloop()








