from lists import *


def greeting_art():
    print(''' 
               █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀████████████████████████████████████████████████████
               ▌██▀▀▀▀███████████████▀▀▀▀██▐*   *   *   *   *   *   *   *   *   *   *   *   * ▐  
               ▌█▌░░░░░░███████████░░░░░░▐█▐  *   *       *   *   *   *   *   *   *   *   *   ▐
               ▌█▌▒▒▒▒░░░▐███████▌░░░▒▒▒▒▐█▐*   *   *   *   *   *   *   *   *   *       *   * ▐
               ▌██▒▒▒▒▒░░░███████░░░▒▒▒▒▒██▐  *   *   *   *   *   *       *   *   *   *   *   ▐
               ▌███▄▄▒▒▒░░███████░░▒▒▒▄▄███▐*   *       *   *   *   *   *   *   *   *   *   * ▐
               ▌█████▌▒▒░░███████░░▒▒▐█████▐  *   *   * Привет! Меня зовут Оникс. *   *   *   ▐
               ▌█████▌▒▒░░▀▀▀▀▀▀▀░░▒▒▐█████▐*    Я сделал общее предсказание на 2023 год.    *▐
               ▌███▀░░░░░░░░░░░░░░░░░░░▀███▐  *   *    Хочешь узнать своё будущее?*   *    *  ▐
               ▌██▌░┌▄┐░░░░░░░░░░░░░┌▄┐░▐██▐*   *   *   *   *   *   *   *   *   *   *   *   * ▐
               ▌██░░└▀┘░░░░░░▄░░░░░░└▀┘░░██▐   *   *   *   *   *   *   *   *   *   *   *   *  ▐
               ▌██▌░░░░░░░░└─┴─┘░░░░░░░░▐██▐*   *   *   *   *   *   *   *   *   *   *   *   * ▐
               ▌████▄▄▄░░░░░░░░░░░░░▄▄▄████▐   *   *   *   *   *   *   *   *   * █ *   *   *  ▐         
               ▌█████▀░░░░░░░░░░░░░░░▀█████▐*   *   *   *   *   *   *   *   *  ▄█▄█▄*   *   * ▐             
               ▌████▌░░└─┐░░░░░░░┌─┘░░▐████▐  *   *   *   *   *   *   *   *   ▄█▀█▄█▄ *   *   ▐             
               ▌█████▄──┘░░░░░░░░░└──▄█████▐*   *   *   *   *   *   *   *   *▄█▀██▀██▄  *   * ▐            
               ▌████▀▀─┐░░░░░░░░░░░┌─▀▀████▐  *   *   *   *   *   *   *   *▄██▀█▄██▀███▄  *   ▐      
               ▌██▀▀░░░░░▒▒▒▒▒▒▒▒▒░░░░░▀▀██▐*   *   *   *   *   *   *   * ▄█▀████▀████▄█▄   * ▐       
               ▌██▄▄▄▄▄█████████████▄▄▄▄▄██▐  *   *   *   *   *   *   *   *   * ███   *   *   ▐                
               ████████████████████████████████████████████████████████████████████████████████''')


def stars_line():
    print('*' * 110)


def is_flag_valid(name):
    while True:
        flag = yes_no(input(f'\n{name}: ').lower())
        if flag == True or flag == False:
            break
        else:
            stars_line()
            print(' ' * 33 + 'Что? Не разобрал. Скажи "да" или "нет".')
            stars_line()
            continue
    return flag


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
    stars_line()
    print(' ' * 40 + 'Скажи, как тебя зовут? ', end='')
    print()
    stars_line()
    name = input('\nТы: ')
    return name.capitalize()


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


def prediction(zodiac):
    """
    предсказание
    :return: строку с индивидуальным предсказанием
    """
    if zodiac == easter_egg[0]:
        return predictions[-1]
    else:
        return predictions[zodiacs.index(zodiac)]


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
    while True:
        try:
            stars_line()
            year = int(input(f'\n{name}: '))
            if 1924 < year < 2024:
                return zodiak[(year-2000) % 12]
            else:
                stars_line()
                print(' '*25 + 'Не думаю, что ты родился именно в этот год. Введи корректный')
                continue
        except ValueError:
            stars_line()
            print(' '*25 + 'Это не похоже на год рождения. Введи корректный.')
            continue
