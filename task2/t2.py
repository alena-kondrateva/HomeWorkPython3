# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

def new_list(size):
    new_list = []
    for el in range(size):
        new_list.append(randint(-size, size))
    return new_list

n = int(input('Задайте длину списка: '))
my_list = new_list(n)
print(my_list)

def multEl(new_list, size):
    new_list2 = []
    for i in range(len(new_list)):
        while i < len(new_list)/2 and size > len(new_list)/2:
            size -= 1
            a = new_list[i] * new_list[size]
            new_list2.append(a)
            i += 1
    return new_list2
    
result = multEl(my_list, n)
print(result)
