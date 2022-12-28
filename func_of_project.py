from lists import *


def greeting_art():
    print(''' 
    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀████████████████████████████████████████████████████
    ▌██▀▀▀▀█████████████▀▀▀▀██▐*   *   *   *   *   *   *   *   *   *   *   *   * ▐  
    ▌█▌░░░░░░█████████░░░░░░▐█▐  *   *       *   *   *   *   *   *   *   *   *   ▐
    ▌█▌▒▒▒▒░░░▐█████▌░░░▒▒▒▒▐█▐*   *   *   *   *   *   *   *   *   *       *   * ▐
    ▌██▒▒▒▒▒░░░█████░░░▒▒▒▒▒██▐  *   *   *   *   *   *       *   *   *   *   *   ▐
    ▌███▄▄▒▒▒░░█████░░▒▒▒▄▄███▐*   *       *   *   *   *   *   *   *   *   *   * ▐
    ▌█████▌▒▒░░█████░░▒▒▐█████▐  *   *   * Привет! Меня зовут Оникс. *   *   *   ▐
    ▌█████▌▒▒░░▀▀▀▀▀░░▒▒▐█████▐*    Я сделал общее предсказание на 2023 год.    *▐
    ▌███▀░░░░░░░░░░░░░░░░░▀███▐  *   *    Хочешь узнать своё будущее?*   *    *  ▐
    ▌██▌░┌▄┐░░░░░░░░░░░┌▄┐░▐██▐*   *   *   *   *   *   *   *   *   *   *   *   * ▐
    ▌██░░└▀┘░░░░░▄░░░░░└▀┘░░██▐   *   *   *   *   *   *   *   *   *   *   *   *  ▐
    ▌██▌░░░░░░░└─┴─┘░░░░░░░▐██▐*   *   *   *   *   *   *   *   *   *   *   *   * ▐
    ▌████▄▄▄░░░░░░░░░░░▄▄▄████▐   *   *   *   *   *   *   *   *   * █ *   *   *  ▐         
    ▌█████▀░░░░░░░░░░░░░▀█████▐*   *   *   *   *   *   *   *   *  ▄█▄█▄*   *   * ▐             
    ▌████▌░░└─┐░░░░░┌─┘░░▐████▐  *   *   *   *   *   *   *   *   ▄█▀█▄█▄ *   *   ▐             
    ▌█████▄──┘░░░░░░░└──▄█████▐*   *   *   *   *   *   *   *   *▄█▀██▀██▄  *   * ▐            
    ▌████▀▀─┐░░░░░░░░░┌─▀▀████▐  *   *   *   *   *   *   *   *▄██▀█▄██▀███▄  *   ▐      
    ▌██▀▀░░░░▒▒▒▒▒▒▒▒▒░░░░▀▀██▐*   *   *   *   *   *   *   * ▄█▀████▀████▄█▄   * ▐       
    ▌██▄▄▄▄▄███████████▄▄▄▄▄██▐  *   *   *   *   *   *   *   *   * ███   *   *   ▐                
    ██████████████████████████████████████████████████████████████████████████████''')


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


def is_valid():
    pass


def yes_no(yesno):
    if yesno == 'да':
        return True
    elif yesno == 'нет':
        return False
    else:
        return None


def description(zodiac):
    """
    описание знака зодиака
    :return: строку с прилагательными
    """
    return descriptions[zodiacs.index(zodiac.lower())]


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


def animals(name):
    year = int(input(f'{name}: '))
    return zodiak[(year-2000)%12]
