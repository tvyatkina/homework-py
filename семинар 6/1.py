# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

#import math

#n = int(input('Введите число N: '))
#def arraySum(n):
#    listN = []
#    for i in range(1, n+1):
#        listN.append((1+1/i)**i)
#    return listN
#print (arraySum(n))
#print(sum(arraySum(n)))

import math

n = int(input('Введите число N: '))
a = list(range(1, n+1))
print(list(map(lambda x: (1+1/x)**x, a)))
print(sum(map(lambda x: (1+1/x)**x, a)))