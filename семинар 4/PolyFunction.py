from random import randint as rI

def PolyFunction():
    k = int(input('Введите максимальную степень многочлена: '))
    eq = ''

    for K in range(k, -1, -1):
        cf = rI(-100, 100)
        if K == k:
            if cf > 0:
                eq += str(cf) + 'x^' + str(K)
            if cf < 0:
                eq += '-' + str(abs(cf)) + 'x^' +  str(K)
        else:
            if cf > 0:
                eq += ' + ' + str(cf) + 'x^' + str(K)
            if cf < 0:
                eq += ' - ' + str(abs(cf)) + 'x^' +  str(K)
    return eq + ' = 0'