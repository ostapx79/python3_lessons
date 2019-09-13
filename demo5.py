# filename demo5.py

import random

num = random.randrange(1, 11)
answer = input('Введите число: ')

if not answer.isdigit():
    print('Введите число')
else:
    answer = int(answer)
    if num < answer:
        print('Больше')
    elif num > answer:
        print('Меньше')
    else:
        print('Правильно!')
