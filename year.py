yearKnow = 2023
yearYou = int(input('В каком году вы родились?: '))
while yearYou < 1826 or yearYou >= 2021:
    print('Не возможно!!!')
    yearYou = int(input('В каком году вы родились?: '))