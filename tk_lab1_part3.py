from tkinter import *

#визначення батьківського класу
class main:
    def __init__(self, master):
        self.master = master
        self.master.title('myWindow')
        self.master.geometry('200x150+200+150')
        child(self.master)
        self.master.mainloop()

#визанчення класу нащадка
class child:
    def __init__(self, master):
        self.slave = Toplevel(master)
        self.slave.title('child')
        self.slave.geometry('200x150+400+300')

#cтворення вікна
root = Tk()
#запуск вікна
main(root)
