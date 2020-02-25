import base64
from tkinter import*


root=None
myText=None
count=0

def buttonPushed():

    global myText
    global count

    count +=1

    myText.set("Stop your clicking, it's already been %d times!" %(count))


def addTextLabel(root):

    global myText

    myText=StringVar()
    myText.set("")
    myLabel=Label(root,textvarible=myText)
    myLabel.pack()

def main():

    global root
    root = Tk()

    mybutton=Button(root,text="show",command=buttonPushed())
    mybutton.pack()
    addTextLabel(root)

    root.mainloop()

