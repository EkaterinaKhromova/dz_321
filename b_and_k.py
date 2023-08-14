# Быки и коровы
from random import choice 
# import random

print('Давай сыграем в игру быки и коровы!\nЗагадано четырехзначное число, попробуй его отгадать!\nБык - цифра на своём месте.\nКорова - цифра не на своём месте.')

stroka = '0123456789'                               
x = choice(stroka[1:10])                             # Создаём строку x из одного случайно выбранного символа из среза stroka (без 0)
for i in range(3):                                   # В цикле из 3-x повторений
    stroka = ''.join(stroka.split(x[i]))             # удаляем из stroka символ который добавили в строку x,
    x += choice(stroka)                              # добавляем к строке x случайно выбранные символы из строки 
xod = 0                                                # Счётчик ходов         
# print(x)     #подсказка/проверка

while True:
    igrok = input("Введите четырёхзначное число: ") 
    if len(igrok) != 4 or not igrok.isdigit():       # проверяем что введенно 4 числа и они цифры
        continue
    
    xod += 1                              
    b = 0;                                               # быки
    c = 0                                                # коровы
    for i in range(4):                                   # В цикле из 4-x повторений
        if x[i] == igrok[i]:                             # проверяем цифра на своём месте,
            b += 1                                       # если да, то добавляем быка,
        elif igrok[i] in x:                              # если нет, проверяем есть ли в загаданном числе эта цифра?
            c += 1                                       # если да, то добавляем корову
    print(igrok + ' содержит ' + str(b) + ' быка и ' + str(c) + ' коровы')
    if b == 4:                                             
        print('Вы победили!', xod, 'ходов')      
        break                             


