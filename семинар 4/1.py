# Вычислить число c заданной точностью *d*

d = float(input('Введите необходимую точность числа: '))
count = 0
for i in range(1, 10000000):
    count = count + 1
    d = d * 10
    if d%1 == 0:
        break
k = 1
x = 0
for k in range(1, 10000000):
    x = x+4*((-1)**(k+1))/(2*k-1)
print(round(x, count))