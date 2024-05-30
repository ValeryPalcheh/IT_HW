rost = int(input('Введите Ваш рост в cм.: '))
ves = int(input('Введите Ваш вес в кг.: '))
bmi = int(ves / ((rost / 100) ** 2))


print(f'Ваш индекс массы тела: {bmi}')
print(f'18{'='*(bmi - 18)}|{'='*(50-bmi)}50')
