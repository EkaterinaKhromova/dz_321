# С помощью только while сделать задачи 2, 3, 4

# 2. Спросить человека размеры поля (х * у), 
# получить их ОДНИМ вводом '7x8', "нарисовать" 
# поле буковками о без использования цикла.
# 3. Нарисовать только границу поля и пустую серединку.
# 4. Вывести на экран таблицу из 4 строк: три товара и сумма без использования цикла

x, y = map(int, input('Введите размеры поля через пробел: ').split())
bykva = 'o'
count = 0
while count < 1:
    stroka = bykva * x + '\n'
    count += 1
    print(stroka * y)