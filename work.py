
import datetime

know = datetime.date.today() #дата (с отсечением времени).
monthYou = int(input('В каком месяце вы устроились? '))

cur_month = know.month # Месяц текущий
b = cur_month - monthYou
know = know.replace(month = monthYou) # меняем только месяц

print('Вы работаете:', b, 'месяц. Устроились', know.strftime('%m.%Y'))

payday = 50000
indexPay = payday + (b * 100)
print('Ваша зп составляет:', indexPay, 'руб.')
vacation =  b * 2
print('У вас накоплено:', vacation, 'дней отпуска')
