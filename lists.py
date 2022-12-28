zodiacs = ['козерог', 'водолей', 'рыбы', 'овен', 'телец', 'близнецы', 'рак',
           'лев', 'дева', 'весы', 'скорпион', 'стрелец']

months = list_months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля',
                        'августа', 'сентября', 'октября', 'ноября', 'декабря']
default = ['Итак, значит ты - ', 'Ага, твой знак зодиака - ', 'Ты - ',
          'Говорят, вы', 'Обычно представители этого знака', 'По стереотипам вы',
          'Согласишься с этим?', 'Как думаешь, подходит?', 'Похоже на тебя?',
          'Кстати, знаешь, твоя стихия -', 'У этого знака стихия -', 'Твоя стихия -',
          'Это круто.', 'Прикольно!', 'Круто же, да?',
          'Интересно, что приготовил для тебя 2023 год...', 'Так, да, предсказание. Что же тебя ждёт...',
          'Чуть не забыл, предсказание. Сейчас соединюсь со Вселенной...',
          'Боги таро утверждают, что', 'Высшие силы твердят:', 'Ого, вот что:']
ranges = [[19, 31],[18, 29],[20, 31],[19, 30],[20, 31],[20, 30],[22, 31],[22, 31],[22, 30],[22, 31],[21, 30],[21, 31]]

descriptions = ['надёжные, прагматичные, организованные, дальновидные и последовательные',
                'свободолюбивые, независимые, честные, справедливые и революционные',
                'непрактичные, непостоянные, мечтательные, сочувствующие и жертвенные',
                'независимые, импульсивные, энергичные, упорные и трудолюбивые',
                'творческие, практичные, расчётливые, целеустремлённые и интересные',
                'коммуникабельные, интеллектуальные, любознательные, жизнерадостные и изобретательные',
                'чувствительные, эмоциональные, интуитивные, проницательные и внимательные',
                'харизматичные, дружелюбные, открытые, сильные и властные',
                'ранимые, терпеливые, трудолюбивые, аккуратные и основательные',
                'уравновешенные, дипломатичные, влюбчивые, неэмоциональные внешне и ранимые',
                'страстные, стойкие, увлечённые, ревнивые и беспокойные',
                'мечательные, рисковые, любознательные, эмоциональные и вспыльчивые']
zodiak = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Кролик. Это же я!"]

easter_egg = ['змееносец']










# Reserve
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
