a = int(input('Enter start distance: '))
b = int(input('Enter target distance: '))
day = int(1)
while a < b:
    print(str(day) + '-й день: ' + "%.2f" % a)
    day += 1
    a *= 1.1
print(str(day) + '-й день: ' + "%.2f" % a)
print('Ответ: на ' + str(day) + ' день спортсмен достиг результата — не менее ' + str(b) + ' км.')
