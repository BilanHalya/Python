#Lab_6_1
#MAde by Halya Bilan
import random
print('Вводимо бажану кількість елементів:')
n=int(input())
f=[random.randint(-1000,1000) for i in range(0,n+1)]
print('Список буде мати вигляд:')
print(f)
n1=0
l=[]
for i in range(0,n+1):
    if f[i]>0:
        l.append(f[i])
    n1=i+1
a=min(l)
print('Мінімальне значення шукаємо серед наступних значень')
print(l)
print('Результат:')
print(a)
