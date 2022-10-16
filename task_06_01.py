# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#  Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

import random

def make_list(number_elem):
    list = [random.randint(10, 99) for i in range(0, number_elem)]
    return list

def clean_list(list):
    list = [list[i] for i in range(1, len(list)) if list[i] > list[i-1]]
    return list

list = make_list(int(input('Введите количество чисел ---> ')))
print(f'Исходный список чисел ---> {list}')
print(f"Список чисел после обработки ---> {clean_list(list)}")