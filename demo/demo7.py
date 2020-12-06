# filename demo7_if_while.py

import random

n1 = random.randrange(1, 11)
n2 = random.randrange(1, 11)

while True:
    answer = input(f'Сколько будет {n1} + {n2} = ')
    test = answer.replace('.', '', 1)
    if not test.isdigit():
        print('Введите число!')
    else:
        break

if answer == test:
    answer = int(answer)
else:
    answer = float(answer)
    
if answer == n1 + n2:
    print('Правильно')
else:
    print('Не правильно')
