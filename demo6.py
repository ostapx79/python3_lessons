# filename demo6_while.py

i = 0
while i < 5:
    print(i, end=' ', sep='\n')
    i += 1
    
i = 0    
while i < 5:
    print(i, end=' ', sep='\n')
    if i == 3:
        break
    i += 1

i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print(i, end=' ')
    