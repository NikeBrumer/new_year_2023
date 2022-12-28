from random import choice
from func_of_project import *

while True:
    greeting_art()
    name = asks_name()
    print(' ' * 10 + f'Рад познакомиться, {name}! А ты знаешь свой знак зодиака? (да/нет) ', end='')
    flag = yes_no(input(f'\n{name}: ').lower())
    if flag:
        print(' ' * 15 + 'Отлично! Скажи свой знак и узнаешь своё будущее: ', end='')
        while True:
            zodiac = input(f'\n{name}: ').lower()
            if zodiac.lower() == easter_egg[0]:
                print(f'Вау! Твоя фамилия, случайно, не Дарвин?\nВ любом случае у меня и для Змееносцев кое-что есть!'
                      '\nЗмееносцы сильные духом, независимые, нарциссичные, верные и честные.'
                      '\nСходится? Твоя стихия - огонь. Круто!'
                      f'\nЧто же ждёт тебя в 2023 году? А вот что: {prediction(zodiac)}') #Здесь будет на 1 элемент списка больше. Последний - змееносец
            elif zodiac not in zodiacs:
                print('Что? Не понял. Повтори, пожалуйста: ', end='')
                continue
            else:
                break
    elif not flag:
        print('\nНичего страшного! Я тебе помогу. Когда у тебя день рождения? \n'
              'Скажи дату(например, 3 октября)')
        birthday = input(f'\n{name}: ').lower()
        # Ввести проверку на соответствие формату (можно прописать в отдельной функции)
        zodiac = determines_zodiac(birthday)
    else:
        print('Что? Не разобрал. Скажи "да" или "нет": ')
        continue
    zodiac = zodiac.capitalize()

    print(f'\n{(choice(default[:3]) + zodiac):^78}\n{choice(default[3:6])} {description(zodiac)}.\n'
          f'{choice(default[6:9])} {choice(default[9:12])} {element(zodiac)}. {choice(default[12:15])}\n'
          f'{choice(default[15:18])}\n{choice(default[18:])} {prediction()}')

    print('\nТы уже знаешь, что символ 2023 года - Кролик.'
          '\nХочешь узнать, кто является смиволом твоего года рождения? ')

    while True:
        flag = yes_no(input(f'{name}: '))
        if flag:
            print('Вот это любознательность!\nСкажи мне год своего рождения и получишь ответ.')
            symbol = animals(name)
            print(f'Символ твоего года - {symbol}')
            break
        if not flag:
            print('\nЧто ж, наверное, ты уже его знаешь.')
            break

    print('Хочешь еще раз получить предсказание?')
    flag = yes_no(input(f'{name}: '))
    if flag:
        continue
    if not flag:
        print(f'\nПока, {name}! Если захочешь вспомнить предсказание или посмотреть предсказание друзьям - возвращайся!')
        break

