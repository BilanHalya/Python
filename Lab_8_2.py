from math import*
def calculate(*n):
    multie=1
    print('Наші параметри наступні:')
    for i in range(len(n)):
        print(n[i])
        if pow(2,i-1)<n[i]<pow(2,i+1):
            d = 0
        else:
            d = 1
    if d == 0:
        print('Наш результат = 0')
    else:
        for i in range(len(n)):
            multie*=n[i]
        print('Наш результат =',multie)
    return multie
calculate(1,3,7)
calculate(7,13,9,20)
