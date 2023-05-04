import numpy as NP
import matplotlib.pyplot as plt

# Функция: f(x) = - 12×^4*sin (cos (x)) - 18×^3 + 5×^2 + 10x - 30

koef = [-12, -18, 5, 10, -30]
limitX = [100, 150]
x = NP.arange(limitX[0], limitX[1], 0.1)
def func(x, a, b, c, d, e):
    return a*x**4*NP.sin(NP.cos(x)) + b*x**3 + c*x**2 + d*x + e

changeX = []
direction = -1

colour = 'r'
def changeColour():
    global colour 
    if colour == 'r':
        colour = 'g'
    else:
        colour = 'r'
    return colour

# Направление

for i in range(len(x) - 1):
    if direction == -1:
        if func(x[i], *koef) < func(x[i+1], *koef):
            changeX.append((x[i], func(x[i], *koef)))
            direction = 1
    else:
        if func(x[i], *koef) > func(x[i+1], *koef):
            changeX.append((x[i], func(x[i], *koef)))
            direction = -1

print(changeX)
print(len(changeX))

# График

rangeX = NP.arange(limitX[0], changeX[0][0], 0.1)
plt.plot(rangeX, func(rangeX, *koef), changeColour())
for i in range(len(changeX)-1):
    rangeX = NP.arange(changeX[i][0], changeX[i+1][0], 0.1)
    plt.plot(rangeX, func(rangeX, *koef), changeColour())
rangeX = NP.arange(changeX[len(changeX)-1][0], limitX[1], 0.1)
plt.plot(rangeX, func(rangeX, *koef), changeColour())
plt.show()