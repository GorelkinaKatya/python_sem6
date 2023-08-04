first_element = int(input('Введите первый элемент: '))
step = int(input('Введите шаг: '))
element_number = int(input('Введите количество элементов: '))

list_1 = []

for i in range(1, element_number + 1):
    list_1.append(first_element + (i - 1) * step)

print(list_1)