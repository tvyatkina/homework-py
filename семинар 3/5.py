# Задайте число - размер списка. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Размер списка: '))

def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

dataPos = list(fib(n))

def fibNeg(n):
    a, b = 0, -1
    for i in range(n):
        yield a
        a, b = b, a + b

dataNeg = list(fibNeg(n+1))
dataNeg.reverse()
data = dataNeg + dataPos

print(data)