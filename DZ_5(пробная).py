
import os


os.system('cls' if os.name == 'nt' else 'clear')
print('Привет!! Это игра Кто хочет стать миллионером!')
name = input('Как тебя зовут? Ответ - ')
os.system('cls' if os.name == 'nt' else 'clear')
print(f'Очень приятно, {name}')
print('Начнем. Первый вопрос на 100 рублей!')
balans = 0
clue1 = 'Звонок другу'
count_clue1 = 1
clue2 = 'Помощь зала'
count_clue2 = 1
clue3 = '50 на 50'
count_clue3 = 1

condition = ['Если ты хочешь ответить сразу - нажми на "1"', 'Если хочешь воспользоваться подсказками - нажми на "2"']

question = ['Кто приходит под Новый год к хорошим детям?', 'Чем едят суп?\n',
            'Во что превращается вода на морозе?','В какой рисунок разрисована зебра?']
answers = ['а.Дед Мороз  б.Баба Яга  в.Милиционер  г.Директор школы', 'а.Вилками  б.Ложками  в.Руками  г.Совочками\n',
           'а. В пар  б. В лед  в. В газ  г. В кисель', 'а. В горошек  б. В цветочек  в. В клеточку  г. В полосочку']
answer = ['а', 'б', 'б', 'г']
answer_not = ['b', 'г', 'г', 'а']
print()
while True:
    print(f'{question[0]}\nОтветы: {answers[0]}')
    print()

    if count_clue1 + count_clue2 + count_clue3 > 0:
        print(f'{condition[0]}\n{condition[1]}')
        print()
        choice = int(input('И так, что ты выбираешь? - '))

        if choice == 1:
            ans1 = input('Ответ - ')

            if ans1 == answer[0]:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Это правильный ответ!')
                balans += 100
                print(f'Твой выйграш: {balans} рублей')
                print()
                print(f'Следующий вопрос на {balans + 100} рублей')
            else:
                print('Это не правельный ответ! Игра окончена')
                break

        elif choice == 2:
            print('У тебя есть подсказки: ')
            if count_clue1 > 0:
                print(f'1. {clue1}')
            if count_clue2 > 0:
                print(f'2. {clue2}')
            if count_clue3 > 0:
                print(f'3. {clue3}')
            tips = int(input('Какую подсказку выбираешь? - '))

            if tips == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Друг подсказал правельный ответ {answer[0]}')
                balans += 100
                count_clue1 -= 1
                print(f'Твой выйграш: {balans} рублей')
                print()
                print(f'Следующий вопрос на {balans + 100} рублей')
                
            elif tips == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Зал подсказал правельный ответ {answer[0]}')
                balans += 100
                count_clue2 -= 1
                print(f'Твой выйграш: {balans} рублей')
                print()
                print(f'Следующий вопрос на {balans + 100} рублей')
                
            elif tips == 3:
                print(f'Выбери правильный ответ из двух вариантов: {answer[0]},  {answer_not[0]}')
                ans1 = input('Ответ - ')
                if ans1 == answer[0]:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Это правильный ответ!')
                    balans += 100
                    count_clue3 -= 1
                    print(f'Твой выйграш: {balans} рублей')
                    print()
                    print(f'Следующий вопрос на {balans + 100} рублей')
                else:
                    print('Это не правельный ответ! Игра окончена')
                    break
            else:
                print(f'Это не правельный ответ! Игра окончена')
                break
            
        else:
            os.system('cls' if os.name == 'nt' else 'clear')     
            print('Не верный ответ') 
            break
    else:
        print('У тебя больше нет подсказок.')
        ans1 = input('Ответ - ')
        if ans1 == answer[0]:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Это правильный ответ!')
            balans += 100
            print(f'Твой выйграш: {balans} рублей')
            print()
            print(f'Следующий вопрос на {balans + 100} рублей')
        else:
            print('Это не правельный ответ! Игра окончена')
            break 
    print()
    print(f'{question[1]}\nОтветы: {answers[1]}')
    print()
    if count_clue1 + count_clue2 + count_clue3 > 0:
        print(f'{condition[0]}\n{condition[1]}')
        print()
        choice = int(input('И так, что ты выбираешь? - '))

        if choice == 1:
            ans1 = input('Ответ - ')

            if ans1 == answer[1]:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Это правильный ответ!')
                balans += 100
                print(f'Твой выйграш: {balans} рублей')
                print()
                print(f'Следующий вопрос на {balans + 100} рублей')
            else:
                print('Это не правельный ответ! Игра окончена')
                break

        elif choice == 2:
            print('У тебя есть подсказки: ')
            if count_clue1 > 0:
                print(f'1. {clue1}')
            if count_clue2 > 0:
                print(f'2. {clue2}')
            if count_clue3 > 0:
                print(f'3. {clue3}')
            tips = int(input('Какую подсказку выбираешь? - '))

            if tips == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Друг подсказал правельный ответ {answer[1]}')
                balans += 100
                count_clue1 -= 1
                print(f'Твой выйграш: {balans} рублей')
                print()
                print(f'Следующий вопрос на {balans + 100} рублей')
                
            elif tips == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Зал подсказал правельный ответ {answer[1]}')
                balans += 100
                count_clue2 -= 1
                print(f'Твой выйграш: {balans} рублей')
                print()
                print(f'Следующий вопрос на {balans + 100} рублей')
                
            elif tips == 3:
                print(f'Выбери правильный ответ из двух вариантов: {answer[1]},  {answer_not[1]}')
                ans1 = input('Ответ - ')
                if ans1 == answer[1]:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Это правильный ответ!')
                    balans += 100
                    count_clue3 -= 1
                    print(f'Твой выйграш: {balans} рублей')
                    print()
                    print(f'Следующий вопрос на {balans + 100} рублей')
                else:
                    print('Это не правельный ответ! Игра окончена')
                    break
            else:
                print(f'Это не правельный ответ! Игра окончена')
                break
            
        else:
            os.system('cls' if os.name == 'nt' else 'clear')     
            print('Не верный ответ') 
            break
    else:
        print('У тебя больше нет подсказок.')
        ans1 = input('Ответ - ')
        if ans1 == answer[1]:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Это правильный ответ!')
            balans += 100
            print(f'Твой выйграш: {balans} рублей')
            print()
            print(f'Следующий вопрос на {balans + 100} рублей')
        else:
            print('Это не правельный ответ! Игра окончена')
            break         
    print()
    print(f'{question[2]}\nОтветы: {answers[2]}')
    print()
    if count_clue1 + count_clue2 + count_clue3 > 0:
        print(f'{condition[0]}\n{condition[1]}')
        print()
        choice = int(input('И так, что ты выбираешь? - '))

        if choice == 1:
            ans1 = input('Ответ - ')

            if ans1 == answer[1]:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Это правильный ответ!')
                balans += 100
                print(f'Твой выйграш: {balans} рублей')
                print()
                print(f'Следующий вопрос на {balans + 100} рублей')
            else:
                print('Это не правельный ответ! Игра окончена')
                break

        elif choice == 2:
            print('У тебя есть подсказки: ')
            if count_clue1 > 0:
                print(f'1. {clue1}')
            if count_clue2 > 0:
                print(f'2. {clue2}')
            if count_clue3 > 0:
                print(f'3. {clue3}')
            tips = int(input('Какую подсказку выбираешь? - '))

            if tips == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Друг подсказал правельный ответ {answer[2]}')
                balans += 100
                count_clue1 -= 1
                print(f'Твой выйграш: {balans} рублей')
                print()
                print(f'Следующий вопрос на {balans + 100} рублей')
                
            elif tips == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Зал подсказал правельный ответ {answer[2]}')
                balans += 100
                count_clue2 -= 1
                print(f'Твой выйграш: {balans} рублей')
                print()
                print(f'Следующий вопрос на {balans + 100} рублей')
                
            elif tips == 3:
                print(f'Выбери правильный ответ из двух вариантов: {answer[2]},  {answer_not[2]}')
                ans1 = input('Ответ - ')
                if ans1 == answer[2]:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Это правильный ответ!')
                    balans += 100
                    count_clue3 -= 1
                    print(f'Твой выйграш: {balans} рублей')
                    print()
                    print(f'Следующий вопрос на {balans + 100} рублей')
                else:
                    print('Это не правельный ответ! Игра окончена')
                    break
            else:
                print(f'Это не правельный ответ! Игра окончена')
                break
            
        else:
            os.system('cls' if os.name == 'nt' else 'clear')     
            print('Не верный ответ') 
            break
    else:
        print('У тебя больше нет подсказок.')
        ans1 = input('Ответ - ')
        if ans1 == answer[2]:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Это правильный ответ!')
            balans += 100
            print(f'Твой выйграш: {balans} рублей')
            print()
            print(f'Следующий вопрос на {balans + 100} рублей')
        else:
            print('Это не правельный ответ! Игра окончена')
            break         
    print()
    print(f'{question[3]}\nОтветы: {answers[3]}')
    print()
    if count_clue1 + count_clue2 + count_clue3 > 0:
        print(f'{condition[0]}\n{condition[1]}')
        print()
        choice = int(input('И так, что ты выбираешь? - '))

        if choice == 1:
            ans1 = input('Ответ - ')

            if ans1 == answer[3]:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Это правильный ответ!')
                balans += 100
                print(f'Твой выйграш: {balans} рублей')
                print()
                print(f'Следующий вопрос на {balans + 100} рублей')
            else:
                print('Это не правельный ответ! Игра окончена')
                break

        elif choice == 2:
            print('У тебя есть подсказки: ')
            if count_clue1 > 0:
                print(f'1. {clue1}')
            if count_clue2 > 0:
                print(f'2. {clue2}')
            if count_clue3 > 0:
                print(f'3. {clue3}')
            tips = int(input('Какую подсказку выбираешь? - '))

            if tips == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Друг подсказал правельный ответ {answer[3]}')
                balans += 100
                count_clue1 -= 1
                print(f'Твой выйграш: {balans} рублей')
                print()
                print(f'Следующий вопрос на {balans + 100} рублей')
                
            elif tips == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Зал подсказал правельный ответ {answer[3]}')
                balans += 100
                count_clue2 -= 1
                print(f'Твой выйграш: {balans} рублей')
                print()
                print(f'Следующий вопрос на {balans + 100} рублей')
                
            elif tips == 3:
                print(f'Выбери правильный ответ из двух вариантов: {answer[3]},  {answer_not[3]}')
                ans1 = input('Ответ - ')
                if ans1 == answer[3]:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Это правильный ответ!')
                    balans += 100
                    count_clue3 -= 1
                    print(f'Твой выйграш: {balans} рублей')
                    print()
                    print(f'Следующий вопрос на {balans + 100} рублей')
                else:
                    print('Это не правельный ответ! Игра окончена')
                    break
            else:
                print(f'Это не правельный ответ! Игра окончена')
                break
            
        else:
            os.system('cls' if os.name == 'nt' else 'clear')     
            print('Не верный ответ') 
            break
    else:
        print('У тебя больше нет подсказок.')
        ans1 = input('Ответ - ')
        if ans1 == answer[3]:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Это правильный ответ!')
            balans += 100
            print(f'Твой выйграш: {balans} рублей')
            print()
            print(f'Следующий вопрос на {balans + 100} рублей')
        else:
            print('Это не правельный ответ! Игра окончена')
            break         
    break

       