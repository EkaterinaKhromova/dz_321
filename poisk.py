# Бинарный поиск: Вы загадываете число от 1 до 1000 
# и записываете его в тетрадь. 
# Компьютер задаёт вам только вопросы типа 
# "число больше 70?" или "число меньше 25?" 
# Вы честно отвечаете "да" или "нет". 
# Компьютер должен угадать ваше число. 
# Сколько попыток ему потребовалось? 
# Это количество зависит от загаданного числа?

input('Загадай число от 0 до 1000! И нажми Enter')
# x = int()
max = int(1000)
min = int(0)
n = int()
hod = 0
while hod != 9:
    n = int((max + min) / 2)
    otvet = input(f'Число больше {n}? ')
    if otvet == 'нет':
        max = n 
        hod +=1
        # print(n, max, min)
    else:
        if otvet == 'да':
            min = n + 1
            hod +=1
            # print(n, max, min)
print('Вы загадали число', max,'Попыток:', hod)