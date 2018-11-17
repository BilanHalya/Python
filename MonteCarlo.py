from math import*
from tkinter import*
from random import*
root = Tk()
root.title('Метод Монте Карло')
root.geometry('600x600')

label=Label(root, text='Графіки кола та квадрата', font='Arial 15')
label.pack(fill=X)

label1=Label(root,  font='Arial 15')
label1.pack(fill=X)

label2=Label(root,  font='Arial 15')
label2.pack(fill=X)

label3=Label(root, font='Arial 15')
label3.pack(fill=X)

canvas=Canvas(root, height=360, width = 480, bg='#F5DEB3')
canvas.pack()

canvas.create_rectangle(90,90,290,290,  outline = 'blue')
canvas.create_oval(90,90,290,290, outline='red')
p=0
def circle():
    ind=0
    for i in range(1,1000):
        x=uniform(90,290)
        y=uniform(90,290)
        if sqrt(pow(x-190,2)+pow(y-190,2))<100:
                canvas.create_oval(x-2,y-2,x+2,y+2,fill='green')
                ind+=1
        else:
                canvas.create_oval(x-2,y-2,x+2,y+2,fill='red')
    ind2=ind/1000
    res = ind2*200*200
    
    result1 = 'Кількість точок в колі:{}'.format(ind)
    label1.configure(text =  result1)
    
    result2 = 'Наближена площа кола:{}'.format(res)
    label2.configure(text =  result2)
    
    result3 = 'Точна площа кола:{}'.format(pi*10000)
    label3.configure(text =  result3)
    
button = Button(root, text='Розрахунок', command = circle)        
button.pack()

button_exit= Button(root, text='Вихід', command = root.destroy)
button_exit.pack()

root.mainloop()
