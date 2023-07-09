# continue и как его избегать
# Перепишите программу, избежав "continue"

# Посчитайте количество верных и неверных ответов, процент ошибок
# ГОРШОЧЕК, НЕ ВАРИ! Поставьте ограничения:
# По количеству заданий
# По максимуму ошибок
# По минимальному проценту ошибок

from random import randint
a = randint(1, 10)
b = randint(1, 10)
count = 0
count1 = 0
vsego_vopr = 0

while count < 6:
    vsego_vopr += 1     
    result = a + b    #резельтат пользователя
    answer = int(input('Сколько будет %(a)i + %(b)i = ' % {'a': a, 'b': b })) #результать компа
    if answer != result:
        count +=1
        print('Нет, попробуй ещё раз ', 'Количество ошибок:', count)
        # print('Пора передохнуть!')
                
    else:  
        count1 +=1  
        #continue        #продолжение цикла
        print('Верно', 'Количество правильных ответов:', count1)
        
    a = randint(1, 10)
    b = randint(1, 10)
    

    vsego = count + count1
    dolya = (vsego / vsego_vopr) * 100
    

    print('Решено', vsego, 'Ошибок:', count)
    print(dolya, '%')
    # g = vsego/count*100