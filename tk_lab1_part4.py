from tkinter import *

#визначення батьківського класу
class Main:
    def __init__(self, master, main_color, child_color ):
        self.master = master
        self.master.title('myWindow')
        self.master.configure(bg = main_color) #задаємо колір для вікна
        self.master.geometry('200x150+200+150') #200 і 150 відступи
        Child(self.master, child_color)
        self.master.mainloop()

#визанчення класу нащадка
class Child:
    def __init__(self, master, child_color):
        self.slave = Toplevel(master)
        self.slave.configure(bg = child_color) #задаємо колір для вікна
        self.slave.title('child')
        self.slave.geometry('200x150+400+300')#400 і 300 відступи

#cтворення вікна
root = Tk()
#запуск вікна
Main(root, 'red','blue')
