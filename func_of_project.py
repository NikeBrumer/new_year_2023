from lists import *


def determines_zodiac(birthday):
    '''
    :param birthday: введенная дата рождения
    :return: соответствующий знак зодиака
    '''
    try:
        while True:
            list_birthday = birthday.split()
            list_birthday[0] = int(list_birthday[0])

            if list_birthday[0] in range(1, ranges[months.index(list_birthday[1])][0] + 1):
                return zodiacs[months.index(list_birthday[1])]
            elif list_birthday[0] in range(ranges[months.index(list_birthday[1])][0] + 1,
                                           ranges[months.index(list_birthday[1])][1]):
                return zodiacs[months.index(list_birthday[1]) + 1]
            else:
                print('Не уверен, что такая дата существует.')
                birthday = input('Введи корректную дату: ')

    except (AttributeError, IndexError):
        return zodiacs[0]


def asks_name():
    print(' ' * 28 + 'Скажи, как тебя зовут? ', end='')
    name = input('\n- Меня зовут: ')
    return name


def asks_zodiac(): #Функция избыточна: она выполняет помимо основной работы (запись в переменную zodiac) другую - отвечает за вывод и запись имени
    name = asks_name()
    print(' ' * 10 + f'Рад познакомиться, {name}! А ты знаешь свой знак зодиака? (да/нет) ', end='')
    while True:  # Убрать в отдельную функцию
        yesno = input(f'\n{name}: ').lower()
        if yesno == 'да':
            print(' ' * 15 + 'Отлично! Скажи свой знак и узнаешь своё будущее: ', end='')
            while True:
                zodiac = input(f'\n{name}: ').lower()
                if zodiac not in zodiacs:
                    print('Что? Не понял. Повтори, пожалуйста: ', end='')
                    continue
                else:
                    break
            break

        elif yesno == 'нет':
            print('\nНичего страшного! Я тебе помогу. Когда у тебя день рождения? \n'
                  'Скажи дату(например, 3 октября)')
            date_of_birthday = input(f'\n{name}: ').lower()
            # Ввести проверку на соответствие формату (можно прописать в отдельной функции)
            zodiac = determines_zodiac(date_of_birthday)
            break
        else:
            print('Что? Не разобрал. Скажи "да" или "нет": ')
            continue
    zodiac = zodiac.capitalize()
    return zodiac


def description():
    """
    описание знака зодиака
    :return: строку с прилагательными
    """
    return 'описание описание описание описание описание описание описание'


def prediction():
    """
    предсказание
    :return: строку с индивидуальным предсказанием
    """
    pass


def element(zodiac):
    """
    стихия
    :return: одну из четырех стихий по ЗЗ
    """
    match zodiac.lower():
        case 'овен' | 'стрелец' | 'лев':
            return 'огонь'
        case 'козерог' | 'дева' | 'телец':
            return 'земля'
        case 'близнецы' | 'весы' | 'водолей':
            return 'воздух'
        case 'рак' | 'скорпион' | 'рыбы':
            return 'вода'
