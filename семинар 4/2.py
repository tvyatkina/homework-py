# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def Mult(n):
    Mult = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Mult.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Mult.append(n)
    return Mult
print(Mult(int(input('Введите натуральное число N: '))))