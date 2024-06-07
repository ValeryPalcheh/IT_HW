import os

os.system('cls' if os.name == 'nt' else 'clear')
print("Добро пожаловать в игру 'Кто хочет стать миллионером'!")
print()
print("Ответьте на вопросы, чтобы выиграть миллион рублей.")
print()

questions = [
    {"question": "Кто приходит под Новый год к хорошим детям?", "options": ("A. Дед Мороз", "B. Баба-Яга", "C. Милиционер", "D. Директор школы"), "answer": "A"},
    {"question": "Чем едят суп?", "options": ("A. Вилками", "B. Ложками", "C. Руками", "D. Совочками"), "answer": "B"},
    {"question": "Что растет на дубе?", "options": ("A. Шишки", "B. Яблоки", "C. Жёлуди", "D. Золотая цепь"), "answer": "C"},
    {"question": "Во что превращается вода на морозе?", "options": ("A. В пар", "B. В лёд", "C. В газ", "D. В кисель"), "answer": "B"},
    {"question": "В какой рисунок разрисована зебра?", "options": ("A. В горошек", "B. В цветочек", "C. В клеточку", "D. В полосочку"), "answer": "D"},
    {"question": "Где не бывает рыбы?", "options": ("A. В реке", "B. В озере", "C. В ухе", "D. В компоте"), "answer": "D"},
    {"question": "На что похожа стрекоза?", "options": ("A. На телевизор", "B. На эскалатор", "C. На вертолет", "D. На шарик"), "answer": "C"},
    {"question": "На чем летает Баба-Яга?", "options": ("A. На венике", "B. На метле", "C. На швабре", "D. На пылесосе"), "answer": "B"},
    {"question": "Что чаще всего вешают на елку?", "options": ("A. Шарики", "B. Кубики", "C. Тюбики", "D. Зубики"), "answer": "A"},
    {"question": "Чем мажут царапины?", "options": ("A. Зелёнкой", "B. Краснёнкой", "C. Белилкой", "D. Чернилкой"), "answer": "A"}

]

bank = 0
clue1 = 'Звонок другу'
count_clue1 = 1
clue2 = 'Помощь зала'
count_clue2 = 1
clue3 = '50 / 50'
count_clue3 = 1
summa_clue = 3
condition = ['Если ты хочешь ответить сразу - нажми на "1"', 'Если хочешь воспользоваться подсказками - нажми на "2"']

for i, k in enumerate(questions):
    print(f'Вопрос: {i + 1}. {k["question"]}')
    for option in k["options"]:
        print(option)

    if summa_clue == 0:

        answer = input("Ваш ответ (A, B, C или D): ")

        os.system('cls' if os.name == 'nt' else 'clear')
        
        if answer.upper() == k["answer"]:
            bank = 1000 * (i + 1)
            print(f'Правильно! Вы выйграли {bank} рублей.')
            print()

        else:
            print("Неправильно. Игра окончена.")
            break

    elif summa_clue > 0:
        print()
        print(f'{condition[0]}\n{condition[1]}')
        print()
        choice = int(input('И так, что ты выбираешь? - '))

        if choice == 1:
            answer = input("Ваш ответ (A, B, C или D): ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if answer.upper() == k["answer"]:
                bank = 1000 * (i + 1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Правильно! Вы выйграли {bank} рублей.')
                print()


        elif choice == 2:
            print(f'У тебя есть {summa_clue} подсказки: ')
            if count_clue1 > 0:
                print(f'1. {clue1}')
            if count_clue2 > 0:
                print(f'2. {clue2}')
            if count_clue3 > 0:
                print(f'3. {clue3}')
                tips = int(input('Какую подсказку выбираешь? - '))

                if tips == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    answer = k["answer"]
                    bank = 1000 * (i + 1)
                    count_clue1 -= 1
                    summa_clue -= 1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'Друг подсказал правильный ответ: {answer}')
                    print(f'Правильно! Вы выйграли {bank} рублей.')
                    print()
                elif tips == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    answer = k["answer"]
                    bank = 1000 * (i + 1)
                    count_clue2 -= 1
                    summa_clue -= 1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'Зал подсказал правильный ответ: {answer}')
                    print(f'Правильно! Вы выйграли {bank} рублей.')
                    print()
                elif tips == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    answer = k["answer"]
                    count_clue3 -= 1
                    summa_clue -= 1 
                    bank = 1000 * (i + 1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'Компьютер подсказал правильный ответ: {answer}')
                    print(f'Правильно! Вы выйграли {bank} рублей.')
                    print() 
                        

print(f'Поздравляем! Вы выйграли {bank} рублей.')
print()