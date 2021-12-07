duration_sec = int(input('Введите количество секунд: '))

if duration_sec <= 59:
    print(duration_sec, 'сек')
elif duration_sec <= 3599:
    print(duration_sec // 60, 'мин', duration_sec % 60, 'сек')
elif duration_sec <= 86399:
    print(duration_sec // 3600, 'ч', duration_sec % 60, 'мин', duration_sec % 60, 'сек')
else:
    duration_sec == 86400
    print('24 часа ровно')