# filename demo1.py

w = input('Введите сторону прямоугольника: ')
h = input('Введите другую сторону: ')

w = int(w)
h = int(h)


# s = 'Площадь прямоугольника {} x {} = {}'.format(w, h, w * h)
s = f'Пдощадь прямоугольника {w} x {h} = {w * h}'
print(s)
