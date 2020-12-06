# filename demo8_if_while.py

import random

number = random.randrange(1, 11)

while True:
    answer = input('Введите число:')

    if not answer.isdigit():
        print('Наберите число') 
        continue

    answer = int(answer)
    if answer < number:
        print('Меньше')
    elif answer > number:
        print('Больше')
    else:
        print('Угадал!')
        break

    
