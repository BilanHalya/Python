import random
def game(x):
    n=random.randint(1,20)
    if x == n:
        print("Так, Ви вгадали!!! Вітаємо!")
    else:
        print("На жаль, Ваша відповідь неправильна")
    print('n=',n)
