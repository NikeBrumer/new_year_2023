from lists import *


def determines_zodiac(birthday):
    '''
    :param birthday: введенная дата рождения
    :return: соответствующий знак зодиака
    '''


    #Здесь 100% возникнет исключение IndexError на стыке декабря и января. Проверить и исправить
    # Проверяю изменение имени в гит. P.S.: Программа думает, что я другой пользователь
    try:
        while True:
            list_birthday = birthday.split()
            list_birthday[0] = int(list_birthday[0])

            if list_birthday[0] in range(1, ranges[months.index(list_birthday[1])][0] + 1):
                return zodiacs[months.index(list_birthday[1])]
            elif list_birthday[0] in range(ranges[months.index(list_birthday[1])][0] + 1, ranges[months.index(list_birthday[1])][1]):
                return zodiacs[months.index(list_birthday[1]) + 1]
            else:
                print('Не уверен, что такая дата существует.')
                birthday = input('Введи корректную дату: ')

    except (AttributeError, IndexError):
        return zodiacs[0]



def questions_zodiak():
    print('Приветствую! Хочешь общее предсказание на новый 2023 год? '
          '\nА ты знаешь свой знак зодиака? (да/нет) ', end='')
    while True:  # Убрать в отдельную функцию
        yesno = input().lower()
        if yesno == 'да':
            print('Отлично! Скажи свой знак и узнаешь своё будущее: ', end='')
            while True:
                zodiac = input().lower()
                if zodiac not in zodiacs:
                    print('Что? Не понял. Повтори, пожалуйста: ', end='')
                    continue
                else:
                    break
            break

        elif yesno == 'нет':
            date_of_birthday = input('Ничего страшного! Я тебе помогу. Когда у тебя день рождения? \n'
                                     'Введи дату(например, 3 октября): ').lower()
            # Ввести проверку на соответствие формату (можно прописать в отдельной функции)
            zodiac = determines_zodiac(date_of_birthday)
            break
        else:
            print('Что? Не разобрал. Введи "да" или "нет": ')
            continue

    return zodiac.capitalize()


def description():
    """
    описание знака зодиака
    :return: строку с прилагательными
    """
    pass


def prediction():
    """
    предсказание
    :return: строку с индивидуальным предсказанием
    """
    pass


def element():
    """
    стихия
    :return: одну из четырех стихий по ЗЗ
    """
    pass
