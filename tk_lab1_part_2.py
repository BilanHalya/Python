from tkinter import*
clk = 0
#визначення функції натиснення кнопки
def btn_click():
    global clk
    lba.config(text = "Натиснена кнопка!",
    bg = '#660066', fg = 'white')
    clk += 1
    root.title("myWindow: {}".format(clk))

#визначення функції, яка визначає кількість кліків по кнопці 
def ent_enter(event):
    global clk
    txt = ent.get()
    lba.config(text = "Текст: " + txt, bg = 'yellow', fg = 'blue')
    clk -= 1
    root.title("myWindow: {}".format(clk))

#створення вікна
root = Tk()
root.title('myWindow:')
root.geometry('200x150+50+50')
#створення рядка вводу
ent = Entry(root)
ent.config(fg = "blue", font = 'Courer_New 10')
ent.insert(0, 'ABCD')
ent.bind('<Return>', ent_enter)
ent.pack(side = TOP)
#cтворення мітки
lba = Label(root)
lba.config(text = 'Мітка')
lba.pack(side = TOP)
#створення кнопки
btn = Button(root)
btn.config(text = 'Натисни мене!',command = btn_click)
btn.pack(side = TOP)
#вивід вікна на екран
root.mainloop()
