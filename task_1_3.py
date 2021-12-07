percent = int(input('Введите количество процентов: '))

if percent % 10 == 1:
    print(percent, 'процент')
elif percent % 10 >= 2 and percent % 10 <= 4:
    print(percent, 'процента')
else:
    print(percent, 'процентов')
