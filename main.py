from random import choice
from func_of_project import *

greeting_art()
name = asks_name()
stars_line()
egg = False
print(' ' * 10 + f'Рад познакомиться, {name}! А ты знаешь свой знак зодиака? (да/нет) ', end='')
print()
while True:
    stars_line()
    flag = yes_no(input(f'\n{name}: ').lower())
    if flag:
        stars_line()
        print(' ' * 23 + 'Отлично! Скажи свой знак и узнаешь своё будущее: ', end='')
        print()
        stars_line()
        while True:
            zodiac = input(f'\n{name}: ').lower()
            stars_line()
            if zodiac.lower() == easter_egg[0]:
                egg = True
                break
            elif zodiac not in zodiacs:
                print('Что? Не понял. Повтори, пожалуйста: ', end='')
                continue
            else:
                break
    elif flag == False:
        stars_line()
        print('\nНичего страшного! Я тебе помогу. Когда у тебя день рождения? \n'
              'Скажи дату(например, 3 октября)')
        stars_line()
        birthday = input(f'\n{name}: ').lower()
        # Ввести проверку на соответствие формату (можно прописать в отдельной функции)
        zodiac = determines_zodiac(birthday)
    else:
        stars_line()
        print('Что? Не разобрал. Скажи "да" или "нет": ')
        continue
    zodiac = zodiac.capitalize()
    if egg:
        print(f'Вау! Твоя фамилия, случайно, не Дарвин?\nВ любом случае у меня и для Змееносцев кое-что есть!'
              '\nЗмееносцы сильные духом, независимые, нарциссичные, верные и честные.'
              '\nСходится? Твоя стихия - огонь. Круто!'
              f'\nЧто же ждёт тебя в 2023 году? А вот что: {prediction(zodiac.lower())}')
    else:
        print(f'\n{(choice(default[:3]) + zodiac):^78}\n{choice(default[3:6])} {description(zodiac)}.\n'
              f'{choice(default[6:9])} {choice(default[9:12])} {element(zodiac)}. {choice(default[12:15])}\n'
              f'{choice(default[15:18])}\n{choice(default[18:])} {prediction(zodiac.lower())}')

    print()
    stars_line()
    print('Ты уже знаешь, что символ 2023 года - Кролик.'
          '\nХочешь узнать, кто является символом твоего года рождения? ')
    stars_line()
    while True:
        flag = yes_no(input(f'\n{name}: '))
        if flag:
            stars_line()
            print('Вот это любознательность!\nСкажи мне год своего рождения и получишь ответ.')
            stars_line()
            symbol = animals(name)
            stars_line()
            print(f'Символ твоего года - {symbol}')
            break
        if not flag:
            stars_line()
            print('Что ж, наверное, ты уже его знаешь.')
            break
    stars_line()
    print('Погадаем заново?')
    stars_line()
    flag = yes_no(input(f'\n{name}: '))
    if flag:
        continue
    if not flag:
        stars_line()
        print(f'Пока, {name}! Захочешь вспомнить предсказание или посмотреть предсказание друзьям - возвращайся!')
        stars_line()
        break

