from math import*
from tkinter import*
from random import*
root = Tk()
root.title('Метод Монте Карло')
root.geometry('500x500')
label=Label(root, text='Графіки кола та квадрата', font='Arial 15')
label.pack(fill=X)

canvas=Canvas(root, height=360, width = 480, bg='#F5DEB3')
canvas.pack()
canvas.create_rectangle(90,90,290,290,  outline = 'blue')
canvas.create_oval(90,90,290,290, outline='red')
p=0
ind=0

for i in range(1,100):
    x=uniform(90,290)
    y=uniform(90,290)
    if sqrt(pow(x-190,2)+pow(y-190,2))<=100:
        canvas.create_oval(x-1,y-1,x+1,y+1,fill='green')
    else:
        canvas.create_oval(x-1,y-1,x+1,y+1,fill='red')
        

root.mainloop()
