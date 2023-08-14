# С помощью только while сделать задачи 2, 3, 4
# 3. Нарисовать только границу поля и пустую серединку.
      
pole = True

while pole:
    size = input('Какого размера поле? 5x6\n')
    pole = 'x' not in size
    if not pole:   # икс присутствует - проверяем числа
        xy = size.split('x')
        print(xy)# функция сплит разрежет строку на список из строк до икса и после икса
        pole = len (xy) != 2 or not xy[0].isdigit() or not xy[1].isdigit()

x = int(xy[0])
y = int(xy[1])
top_bottom = 'O' * y + '\n'
middle = ('O' + (' ' * (y - 1 - 1)) + 'O' + '\n') * (x - 1 -1)
print(top_bottom + middle + top_bottom)