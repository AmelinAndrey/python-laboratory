# вводим значения в лист и преобразовываем их в число с плавающей точкой
list = [float(input('1st')),float(input('2nd')),float(input('3th'))]

# вводим переменную shetчик
shet = 0

# создаем инструкцию с перебором и условием для всех єлементов list, а так же выводим необходимые нам значения
for i in list:
    if i==abs(i):
        list[shet] = i**2
        print('елемент '+str(shet+1),'=',i,'при возведении в квадрат =',list[shet])
        shet += 1
    else:
        list[shet] = i**4
        print('елемент '+str(shet+1),'=',i,'при возведении в 4-ую степень =',list[shet])
        shet += 1