
# Импорт модуля содержащий константу пи
import math as m

# инструкция для ввода данных пользователем и преобразование в тип числа с плавающей точкой
a = float(input('insert value'))

#выделение целых частей и округление самых малых единиц измерения
dh = int(a/m.pi*180)
mi = int((a/m.pi*180-dh)*60)
se = round(((a/m.pi*180-dh)*60-mi)*60)

# развлетвление для выбора наиболее лаконичной формы вывода данных
if not int(a)-a:
    print(str(int(a))+'rad '+'= '+str(dh)+ 'hours or degrees '+str(mi)+ 'minutes '+str(se)+ 'seconds')

else:
    print(str(a) + 'rad ' + '= ' + str(dh) + 'hours or degrees ' + str(mi) + 'minutes ' + str(se) + 'seconds')