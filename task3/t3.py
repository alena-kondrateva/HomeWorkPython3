# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

from random import uniform


def new_list(n):
    new_list = []
    for _ in range(n):
        el = uniform(1, 10)
        new_list.append(round(el, 2))
    return new_list


size = int(input('Задайте размер списка: '))
my_list = new_list(size)
print(my_list)


def difference(new_list):
    for i in range(len(new_list)):
        new_list[i] -= int(new_list[i])
    max = 0
    min = new_list[0]
    for i in range(len(new_list)):
        if max < new_list[i]:
            max = new_list[i]
        if min > new_list[i]:
            min = new_list[i]
    res = max - min
    return res


print(round(difference(my_list), 2))
