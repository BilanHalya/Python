#Lab_4, Task 1
#Bilan Halyna
# AMM-2
print("Вивчаємо використання циклу while")
print("Обчислюємо суму наступного ряду до деякого значення m")
m=int(input('m='))
a=0
n=0
k='Початкове значення n='+repr(n)
l='Обчислюємо значення суми до'+repr(m)+' і отримуємо:'
print(k)
print(l)
while n<m:
    a+=1/((3*n-2)*(3*n+1))
    n=n+1
s='result='+repr(a)
print(s)


    
