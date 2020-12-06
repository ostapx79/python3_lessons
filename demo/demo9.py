# filename demo9_if_while.py

import random

number = random.randrange(1, 11)
flag = True

while flag:
    answer = input('Введите число: ')
    if not answer.isdigit():
        print('Введите число а не буквы!')
    else:
        answer = int(answer)
        if answer < number:
            print('Меньше')
        elif answer > number:
            print("Больше")
        else:
            print('Угадали')
            flag = False
