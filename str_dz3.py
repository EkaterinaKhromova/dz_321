# Нарисовать только границу поля и пустую серединку.

x, y = map(int, input('Введите размеры поля через пробел: ').split())

for i in range(1, y + 1):
    if i == 1 or i == y:
        print('*' * x)
    else:
        print('*' + " " * (x - 2) + '*')