#LAB_5
#Made by Halyna Bilan , AMM-2
print('Вчимося використовувати перебір за допомогою for ')
print('Перевірити чи факторіал числа n можна подати через добуток 3 послідовних натуральних чисел')
from math import*
print('Вводимо наше число n')
n=int(input('n='))
fac=factorial(n)
d=0
if n>=3:
    for n in range(1,n+2):
       d=n*(n-1)*(n-2)
       if d==fac:
           print('Можна подати')
           print(n,'*',n-1,'*',n-2,'=',fac,'=',d)
           break
    else:
        print('Не можна подати')
        print(fac,'/=',d)
else:
    print('Не можна подати')


    
