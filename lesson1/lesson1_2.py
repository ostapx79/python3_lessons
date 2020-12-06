#!/usr/bin/python3
#: python3_lessons/lesson1/lesson1_2.py

# ссылка на ячейку в память П/К (переменная)
# и типы данных

numb = 32 # целое число
strings = 'hello' # срока
strings_s = "world" # тоже строка
float_f = .4 # вещественные числа
lists = [numb, strings, strings_s, float_f] # список
tuple_t = (3, ) # кортеж из одного элемента
dict_d = {'tuple': tuple_t, 'list': lists} # словарь из двух элементов

print(numb)
print(strings)
print(strings_s)
print(float_f)
print(lists)
print(tuple_t)
print(dict_d)
