import random
n=10
day=[random.randint(1,31) for i in range(0,10)]
month=[random.randint(1,12) for i in range(0,10)]
year=[1930 for i in range (0,10)]
xy=zip(day,month,year)
xy=list(xy)
print(xy)
L=[]
for i in range(1, n+1):
 a='Date'+str(i)
 L.append(a)
D={k:v for (k,v) in zip(L,xy)}
print('Наші дати:')
print (D)
print('Введіть першу дату для порівняння')
num1=input()
print('Введіть другу дату для порівняння')
num2=input()
d1=list(D.get(num1))
d2=list(D.get(num2))
print('Перша дата така:')
print(d1)
print('Друга дата така:')
print(d2)
if d1[1]<d2[1]:
    print('Перша дата відбулася швидше')
else:
    if d1[0]<d2[0]:
        print('Перша дата відбулася швидше')
    else:
        print('Друга дата відбулася швидше')
    

