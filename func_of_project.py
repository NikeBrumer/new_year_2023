from lists import *


def determine_zodiak(birthday):
    '''
    :param birthday: введенная дата рождения
    :return: соответствующий знак зодиака
    '''

    list_birthday = birthday.split()
    list_birthday[0] = int(list_birthday[0])
    #Здесь 100% возникнет исключение IndexError на стыке декабря и января. Проверить и исправить
    # Проверяю изменение имени в гит
    if list_birthday[0] in range(1, ranges[months.index(list_birthday[1])][0] + 1):
        return zodiaks[months.index(list_birthday[1])]
    elif list_birthday[0] in range(ranges[months.index(list_birthday[1])][0] + 1, ranges[months.index(list_birthday[1])][1]):
        return zodiaks[months.index(list_birthday[1])+1]
    # if (21 < int(list_birthday[0]) < 32 and list_birthday[1] == months[11]) \
    #         or (0 < int(list_birthday[0]) < 20 and list_birthday[1] == months[0]):
    #     return zodiaks[0]  # Козерог.
    # if (19 < int(list_birthday[0]) < 32 and list_birthday[1] == months[0]) \
    #         or (0 < int(list_birthday[0]) < 19 and list_birthday[1] == months[1]):
    #     return zodiaks[1]  # Водолей.
    # if (18 < int(list_birthday[0]) < 30 and list_birthday[1] == months[1]) \
    #         or (0 < int(list_birthday[0]) < 21 and list_birthday[1] == months[2]):
    #     return zodiaks[2]  # Рыбы.
    # if (20 < int(list_birthday[0]) < 32 and list_birthday[1] == months[2]) \
    #         or (0 < int(list_birthday[0]) < 20 and list_birthday[1] == months[3]):
    #     return zodiaks[3]  # Овен.
    # if (19 < int(list_birthday[0]) < 32 and list_birthday[1] == months[3]) \
    #         or (0 < int(list_birthday[0]) < 21 and list_birthday[1] == months[4]):
    #     return zodiaks[4]  # Телец.
    # if (20 < int(list_birthday[0]) < 32 and list_birthday[1] == months[4]) \
    #         or (0 < int(list_birthday[0]) < 21 and list_birthday[1] == months[5]):
    #     return zodiaks[5]  # Близнецы.
    # if (20 < int(list_birthday[0]) < 32 and list_birthday[1] == months[5]) \
    #         or (0 < int(list_birthday[0]) < 23 and list_birthday[1] == months[6]):
    #     return zodiaks[6]  # Рак.
    # if (22 < int(list_birthday[0]) < 32 and list_birthday[1] == months[6]) \
    #         or (0 < int(list_birthday[0]) < 23 and list_birthday[1] == months[7]):
    #     return zodiaks[7]  # Лев.
    # if (22 < int(list_birthday[0]) < 32 and list_birthday[1] == months[7]) \
    #         or (0 < int(list_birthday[0]) < 23 and list_birthday[1] == months[8]):
    #     return zodiaks[8]  # Дева.
    # if (22 < int(list_birthday[0]) < 32 and list_birthday[1] == months[8]) \
    #         or (0 < int(list_birthday[0]) < 23 and list_birthday[1] == months[9]):
    #     return zodiaks[9]  # Весы.
    # if (22 < int(list_birthday[0]) < 32 and list_birthday[1] == months[9]) \
    #         or (0 < int(list_birthday[0]) < 22 and list_birthday[1] == months[10]):
    #     return zodiaks[10]  # Скорпион
    # if (21 < int(list_birthday[0]) < 32 and list_birthday[1] == months[10]) \
    #         or (0 < int(list_birthday[0]) < 22 and list_birthday[1] == months[11]):
    #     return zodiaks[11]  # Стрелец.


def questions_zodiak():
    print('Приветствую! Хочешь общее предсказание на новый 2023 год? '
          '\nА ты знаешь свой знак зодиака? (да/нет) ', end='')
    while True:  # Убрать в отдельную функцию
        yesno = input().lower()
        if yesno == 'да':
            print('Отлично! Скажи свой знак и узнаешь своё будущее: ', end='')
            while True:
                zodiak = input().lower()
                if zodiak not in zodiaks:
                    print('Что? Не понял. Повтори, пожалуйста: ', end='')
                    continue
                else:
                    # print(zodiak.capitalize())
                    break
            break

        elif yesno == 'нет':
            date_of_birthday = input('Ничего страшного! Я тебе помогу. Когда у тебя день рождения? \n'
                                     'Введи дату(например, 3 октября): ').lower()
            # Ввести проверку на соответствие формату (можно прописать в отдельной функции)
            zodiak = determine_zodiak(date_of_birthday)
            break
        else:
            print('Что? Не разобрал. Введи "да" или "нет": ')
            continue

    return zodiak.capitalize()


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
