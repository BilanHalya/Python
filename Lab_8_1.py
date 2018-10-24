def tower (n,a,b,c):
    if n != 0:
        tower(n-1,a,c,b)    
        print('{} go to  {}'.format(a,b))  
        tower(n-1,c,b,a)    

n = int(input("введіть кількість дисків: "))

tower(n,1,2,3)
