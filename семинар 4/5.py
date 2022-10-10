# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from PolyFunction import PolyFunction

def dictEq():
    Eq = PolyFunction()
    dict = {}

    Eq = Eq.replace(' + ', ' +').replace(' - ', ' -').split()[:-2]
    for i in range(len(Eq)):
        Eq[i] = Eq[i].replace('+', '').split('x^')
        dict[int(Eq[i][1])] = int(Eq[i][0])
    return dict

dict1 = dictEq()
print(dict1)
dict2 = dictEq()
print(dict2)

dictSum = {}

for i in range(max(len(dict1), len(dict2)), -1, -1):
    dictF = dict1.get(i)
    dictS = dict2.get(i)
    if dictF != None or dictS != None:
        dictSum[i] = (dictF if dictF != None else 0) + (dictS if dictS != None else 0)
print(dictSum)

def eqFinal():
    eq = ''
    for key,value in dictSum.items():
        CF = value
        D = key
        if D != len(dictSum):       # я еще попробую понять, как сделать тут нормально, потому что очвевидно, что есть ошибки
            if CF > 0:
                eq += ' + ' + str(CF)  + 'x^' + str(D)
            if CF < 0:
                eq += ' - ' + str(abs(CF)) + 'x^' + str(D)
        else:
            if CF > 0:
                eq += str(CF)  + 'x^' + str(D)
            if CF < 0:
                eq += ' - ' + str(abs(CF)) + 'x^' + str(D)
    return eq + ' = 0'

eqF = eqFinal()
print(eqF.replace('x^1', 'x').replace('x^0', '').replace('1x', 'x'))