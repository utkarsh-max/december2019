from tkinter import *


def msg():
    print("LEFT Click Me")
class MyGui:

    def __init__(self,master):
        self.btn=Button(master,text="Right Click Me",fg="red",bg="yellow",
            font=("Ariel",12,'bold'),command=msg)
        self.btn.pack()

root=Tk()
ob=MyGui(root)

root.geometry("400x400+400+200")
root.resizable(0,0)
mainloop()
