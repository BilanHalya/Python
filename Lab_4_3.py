#Lab_4 Task 3
#AMM-2 Bilan Halyna
from math import*
print('Вивчаємо механізм використання циклу while')
print('Обчислюємо квадратний корінь за ітераційною формулою Герона')
print("Задаємо число, чий корінь квадратний маємо відшукати ")
a=float(input('a='))
print("Задаємо початкове значення ")
x=float(input('x='))
eps=0.0001
s=0
while abs((x ** 2)- a ) > eps:
    x = (1/2)*(x + a/x)
    s+= 1
print('result= ', float(x),'n=', s)
print('Давайте перевіремо за звичайною формулою:')
k= sqrt(a)
print('result=', float(k))
  
