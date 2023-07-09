# print(1/0)  # падает с ошибкой
# result = 0
# znam = int(input('Введите число, я найду обратное:'))
# try:
#     result = 1 / znam
# except ZeroDivisionError:
#     result = None
# if result:
#     print('Обратное равно ', result)
year = None
while year == None:
    try:
        year = int(input('Введите год рождения: '))
        assert year < 2024 and year > 1800, 'Ты - исторический персонаж?'
    except ValueError:
        print('Год рождния надо вводить цифрами!')
        assert 

if year:
    print(2023 - year)
