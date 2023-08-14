# С помощью только while сделать задачи 2, 3, 4

# 2. Спросить человека размеры поля (х * у), 
# получить их ОДНИМ вводом '7x8', "нарисовать"

x, y = map(int, input('Введите размеры поля через пробел: ').split())
bykva = 'o'
count = 0
while count < 1:
    stroka = bykva * x + '\n'
    count += 1
    print(stroka * y)
