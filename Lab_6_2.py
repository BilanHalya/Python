print('НАш рядок')
text=input()
print('Перший 5 елементів')
a=text[0:5]
print(a)
print('БЕз 2 останніх едементів')
b=text[0:-2]
print(b)
print('Тільки парні індекси')
c=text[0::2]
print(c)
print('Зворотній порядок через один')
d=text[::-2]
print(d)
print('Довжина')
e=len(text)
print(e)
