
import datetime

know = datetime.date.today() #дата (с отсечением времени).
monthYou = int(input('В каком месяце вы устроились? '))

сur_year = know.year # Год текущий
cur_month = know.month # Месяц текущий
b = cur_month - monthYou
know = know.replace(month = monthYou) # меняем только месяц
if monthYou > cur_month:
    yearYou = int(input('Введите год в котором вы устроились: '))
    know.year - yearYou
    b = cur_month + (12 - monthYou)
    print('Вы работаете:', b, 'месяц. Устроились', monthYou,'.',yearYou)#.strftime('%m.%Y'))
else:
    print('Вы работаете:', b, 'месяц. Устроились', know.strftime('%m.%Y'))

payday = 50000
indexPay = payday + (b * 100)
print('Ваша зп составляет:', indexPay, 'руб.')
vacation =  b * 2
print('У вас накоплено:', vacation, 'дней отпуска')
