# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

n = int(input('Введите цифру от 1 до 7: '))

if (n == 6) or (n == 7):
    print('Выходной день')
else:
    print('Будний день')