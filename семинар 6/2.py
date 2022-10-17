# Задайте рандомно список из чисел размером N, где N число с клавиатуры. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#import random

#n = int(input('Введите размер списка: '))
#listN = []
#for i in range(n):
#    listN.append(random.randint(0, 10))
#print('Список: ', listN)
#sum = 0
#for i in range(n):
#    if i%2 != 0:
#        a = int(listN[i])
#        sum = sum+a
#print('Сумма нечетных элементов: ', sum)

def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")

lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)