# Задайте рандомно список из чисел размером N, где N число с клавиатуры. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random

n = int(input('Введите размер списка: '))
listN = []
for i in range(n):
    listN.append(random.randint(0, 10))
print('Список: ', listN)
sum = 0
for i in range(n):
    if i%2 != 0:
        a = int(listN[i])
        sum = sum+a
print('Сумма нечетных элементов: ', sum)