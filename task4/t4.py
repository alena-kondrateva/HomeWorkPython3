# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# num = int(input('Введите число: '))
# print(bin(num))

def convert(n):
    new_list = []
    while n != 0:
        s = n % 2
        new_list.append(s)
        n = n // 2
    print(*new_list[::-1])


num = int(input('Введите число: '))
result = convert(num)
