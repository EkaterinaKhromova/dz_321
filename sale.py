tarif = {'hour' : 60,
         'week' : 300,
         'month' : 1000,
         'year' : 10000 }

vozrast = int(input('Какой у вас год рождения? '))
vozrast_yers =  2023 - vozrast 
if (vozrast_yers > 50) or (vozrast_yers < 14):
    print('Для вас проезд бесплатный!')
if (vozrast_yers >= 14) and (vozrast_yers <= 24):
    print('У вас скидка 50%')
    your_tarif = input('Какой проездной вам нужен? ')
    x = tarif[your_tarif] / 2
    print('Стоимость будет', x, 'рублей')
else:
    your_tarif = input('Какой проездной вам нужен? ')
    x = tarif[your_tarif]
    print('Стоимость будет', x, 'рублей')


