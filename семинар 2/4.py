# Реализуйте алгоритм перемешивания списка.

import random

listL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print('Изначальный список: ', listL)
listN = []
for i in range(len(listL)):
    j = random.randrange(len(listL))
    listN.append(listL[j])
    listL.remove(listL[j])
print('Перемешанный список: ', listN)