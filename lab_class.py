import random
class Month:
    #result=[]
    def __init__(self,number):
        self.number=number
        self.days=[]
        self.a=[random.randint(1,31) for i in range(0,31)]
        self.b=[random.randint(-35,35) for i in range(0,31)]
        self.c=[random.choices(['sunny','rain','cloudy']) for i in range(0,31)]
        self.abc=zip(self.a,self.b,self.c)
        self.result=list(self.abc)
    def __str__(self):
        return 'Наші дані: {}'.format(self.result)
    def checking(self):
        sum=0
        for i in range(0,31):
            sum=self.b[i]
            sum+=sum
        av=sum/31
        print("Середня температура повітря:", av, "градусів")
    def check_sun(self):
        n1=0
        for i in range(0,31):
            if self.c[i] == ['sunny']:
                n1=n1+1
        print("Сонячний днів було: ",n1)
        return(n1)
       
    
    def check_rain(self):
        n2=0
        for i in range(0,31):
             if self.c[i] == ['rain']:
                n2=n2+1
        print("Дощових днів було:",n2)
        return(n2)
        
    def check_cloudy(self):
        n3=0
        for i in range(0,31):
            if self.c[i] == ['cloudy']:
                n3=n3+1
        print("Хмарних днів було:",n3)
        return(n3)
k=Month(4)
print(k)
k.checking()
k.check_sun()
k.check_cloudy()
k.check_rain()
#Month.count_sunny()
