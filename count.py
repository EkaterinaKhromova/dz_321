# С клавиатуры вводятся числа. 
# Остановиться, как только введён ноль. 
# Посчитать количество введенных чисел

number = int(input('Введите число: '))
count = 0
while number != 0:
    count += 1
    print('Количество введенных чисел:',count)
    number = int(input('Введите число: '))