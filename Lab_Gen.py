from math import*
def f(x,ep):
    
    k = 2
    x1=x
    print("Наше значення: ",x1,"крок: 1")
    while True:
        yield x1
        if x1 > ep:
            print("Наше значення: ",x1,"крок: ", k)
            x1 = pow(x,k)/factorial(k)
            k+=1 
        else:
            print("Наше значення: ",x1,"крок: ", k)
            print('Завершення обрахунку')
            break
s=0
for e in f(0.5,0.1):
    s=s+e
print(s)

