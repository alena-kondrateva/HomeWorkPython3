# Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint


def new_list(size):
    n_list = []
    for el in range(n):
        n_list.append(randint(-n, n))
    return n_list


n = 10
my_list = new_list(n)
print(my_list)


def result_sum(new_list):
    sumEl = 0
    for i in range(1, len(new_list), 2):
        sumEl += new_list[i]
    return sumEl


print(result_sum(my_list))
