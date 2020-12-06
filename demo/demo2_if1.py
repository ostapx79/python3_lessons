# filename demo2_if1.py

import random

n1 = random.randrange(1, 11)
n2 = random.randrange(1, 11)

answer = input(f'Сколько будет {n1} + {n2} = ?: ')
answer = int(answer)

if answer == n1 + n2:
    print('Правильно')
else:
    print('Не правильно')

