# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности

from random import randint as rI

listUnique = {}
strUnique = ''

strNum = "".join(list(map(str, [rI(0, 9) for i in range(30)])))
print('Заданная последовательность цифр: ', strNum)

for n in strNum:
    if listUnique.get(n):
        listUnique[n] = listUnique.get(n) + 1
    else:
        listUnique[n] = 1

for i in listUnique.items():
    if i[1] == 1:
        strUnique += str(i[0])

if strUnique:
    print('Уникальные элементы заданной последовательности: ', strUnique)
else:
    print('Уникальных элементов нет.')