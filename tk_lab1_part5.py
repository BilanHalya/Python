from tkinter import *

class Main:
    def __init__(self, master):
        self.master = master
        self.master.title('parent')
        self.master.geometry('200x150+300+225')
        self.button = Button(self.master,text = 'myButton',command = self.openDialog)
        self.button.pack(side = BOTTOM)
        self.master.mainloop()
    def openDialog(self):
        Child(self.master)


class Child:
    def __init__(self, master):
        self.slave = Toplevel(master)
        self.slave.title('child')
        self.slave.geometry('200x150+500+375')
        self.slave.grab_set() #функція, що не дозволяє переходити на батьківське вікно
        self.slave.focus_set()
        self.slave.wait_window()

root = Tk()
Main(root)
