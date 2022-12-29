from random import choice
from func_of_project import *

greeting_art()

while True:
    name = asks_name()
    stars_line()
    egg = False
    print(' ' * 20 + f'Рад познакомиться, {name}! А ты знаешь свой знак зодиака? (да/нет) ', end='')
    print()
    stars_line()

    flag = is_flag_valid(name)

    if flag:
        stars_line()
        print(' ' * 30 + 'Отлично! Скажи свой знак и узнаешь своё будущее.')
        stars_line()
        while True:
            zodiac = input(f'\n{name}: ').lower()
            stars_line()
            if zodiac.lower() == easter_egg[0]:
                egg = True
                break
            elif zodiac not in zodiacs:
                print(' ' * 33 + 'Что? Не понял. Повтори, пожалуйста.')
                stars_line()
                continue
            else:
                break
    elif not flag:
        stars_line()
        print(' ' * 22 + 'Ничего страшного! Я тебе помогу. Когда у тебя день рождения?')
        print(' ' * 33 + 'Скажи дату(например, 3 октября)')
        stars_line()
        birthday = input(f'\n{name}: ').lower()
        stars_line()
        # Ввести проверку на соответствие формату (можно прописать в отдельной функции)
        zodiac = determines_zodiac(birthday)
    zodiac = zodiac.capitalize()
    if egg:
        print(f'Вау! Твоя фамилия, случайно, не Дарвин?\nВ любом случае у меня и для Змееносцев кое-что есть!'
              '\nЗмееносцы сильные духом, независимые, нарциссичные, верные и честные.'
              '\nСходится? Твоя стихия - огонь. Круто!'
              f'\nЧто же ждёт тебя в 2023 году? А вот что: {prediction(zodiac.lower())}')
    else:
        print(f'\n{(choice(default[:3]) + zodiac):^110}\n{choice(default[3:6])} {description(zodiac)}.\n'
              f'{choice(default[6:9])} {choice(default[9:12])} {element(zodiac)}. {choice(default[12:15])}\n'
              f'{choice(default[15:18])}\n{choice(default[18:])} {prediction(zodiac.lower())}')

    print()
    stars_line()
    print(' ' * 31 + 'Ты уже знаешь, что символ 2023 года - Кролик.'
                     '\n' + ' ' * 24 + 'Хочешь узнать, кто является символом твоего года рождения? ')
    stars_line()
    flag = is_flag_valid(name)
    if flag:
        stars_line()
        print(' ' * 35 + 'Вот это любознательность!')
        print(' ' * 25 + 'Скажи мне год своего рождения и получишь ответ.')
        symbol = animals(name)
        stars_line()
        print(' ' * 35 + f'Символ твоего года - {symbol}')
    if not flag:
        stars_line()
        print(' ' * 33 + 'Что ж, наверное, ты уже его знаешь.')

    stars_line()
    print(' ' * 40 + 'Погадаем заново?')
    stars_line()
    flag = is_flag_valid(name)
    if flag:
        stars_line()
        stars_line()
        continue
    if not flag:
        stars_line()
        print(' ' * 15 + f'Пока, {name}! Захочешь вспомнить предсказание или посмотреть предсказание друзьям - возвращайся!')
        stars_line()
        break
