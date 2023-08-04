list_number = int(input('Введите количество элементов: '))
min_ = int(input('Введите минимум: '))
max_ = int(input('Введите максимум: '))

from random import randint
list_1 = [randint(-5, 5) for i in range(0, list_number)]
print(f'Начальный список: {list_1}')

list_2 = []

for i in range(len(list_1)):
    if min_ < list_1[i] < max_:
        list_2.append(i)

print(f'Индексы элементов по условию: {list_2}')