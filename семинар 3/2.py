# Напишите программу, которая найдёт произведение пар чисел списка (Cписок создаем как в предыдущем задании). 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

n = int(input('Введите размер списка: '))
listN = []
for i in range(n):
    listN.append(random.randint(1, 10))
print('Список: ', listN)
for i in range(n):
    if i == n:
        break
    a = int(listN[i]) * int(listN[n-1])
    n = n-1
    print('Произведение пар: ', a, end = ', ')
    if i == n:
        break