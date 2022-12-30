  Программа "Предсказание на 2023"
  -

  (25.12.2022: Данный проект включает в себя все изученные темы в 2022 и является итоговым на момент текущего года)

Как работает программа:

1. Пользователь вводит знак зодиака, если знает его.
2. Если не знает, вводит день рождения (в формате "5 января")
3. Программа выводит текст с предсказанием и спрашивает, хочет ли пользователь узнать символ по году рождения.
4. Пользователь соглашается или отказывается.
5. Если соглашается, то вводит год рождения.
6. Программа выдает ответ в виде названия животного.
7. После основной части программа спрашивает, хочет ли пользователь получить предсказание еще раз.
8. Если пользователь соглашается, то возвращается к первоначальной точке.
9. При отказе программа завершается.
   
Фичи:
- Программа запрашивает имя пользователя и запоминает его
- Программа преобразует любое имя, используя его с заглавной буквы
- Если зодиак с опечаткой или другое - повторный ввод (импрув: добавить слово по маске и уточнение)
- Добавлены прилагательные к знаку зодиака
- Определена стихия
- Пасхалка: Змееносец
- Тексты обращения составляются рандомно для разнообразия
- Для каждого ЗЗ свое предсказание, сделанное заранее
- красивое оформление в консоли
- Определение животного-символа по году рождения
- Запрос на повторное предсказание

  24.12.2022: На данный момент в программе написан такой функционал:
  26.12.2022
  27.12.2022
  28.12.2022
  29.12.2022

- вопрос пользователю, знает ли он свой знак зодиака; (24.12.2022)
  - если да: просьба ввести свой знак зодиака; (24.12.2022)
  - если нет: определение знака зодиака по дате рождения; (24.12.2022)
- проверка валидности ответа да/нет; (24.12.2022)
  - если введено "да" или "нет" в любом регистре - программа выполняется дальше; (24.12.2022)
  - если введено что-то иное - просьба ввести еще раз до тех пор, пока программа не получит валидный ответ; (24.12.2022)
- проверка валидности введенного знака зодиака: (24.12.2022)
    - если валидно, то запись ответа в переменную zodiac; (24.12.2022) 
    - если невалидно, то просьба ввести валидный ответ циклично; (24.12.2022)
- список дефолтного повествования и рандомный выбор по диапазонам;
- проверка валидности введенной даты рождения: (26.12.2022)
  - если валидно, то запись в переменную zodiac; (26.12.2022)
  - если не валидно, то просьба ввести валидную дату рождения (26.12.2022)
- текст вывода: дефолтный текст + знак зодиака + стихия + прилагательные + предсказание;(26.12.2022)
- определение стихии по знаку зодиака (27.12.2022)
- запрос имени у пользователя и использование в обращении и вводе (27.12.2022)
- вывод картинки и частичное форматирование (27.12.2022)
- функция прилагательных к ЗЗ (27.12.2022)
- функция определения символа года (27.12.2022)
- функция да/нет вынесена отдельно (используется неоднократно) (27.12.2022)
- вопрос пользователю, хочет ли еще раз предсказание (27-28.12.2022)
- пасхалка про змееносца; (частично) (28-29.12.2022)
- функция с непосредственными предсказаниями; (29.12.2022)
- итоговое оформление (29.12.2022)



  Что нужно сделать:
- обнаружить и починить баги

  Баги:
- Когда пользователь вводит число без месяца, программа работает (исправлено)
- Когда пользователь вводит невалидную дату, вызывается исключение ValueError. Нужно выполнять проверку на валидность и зацикливать
  до верного ввода (исправлено)
- Скорее всего будет вызвано исключение, если пользователь введет вместо года (число)  - строку (исправлено)
- Программа работает с любым годом, даже невозможным. Поставить граничные значения (исправлено)
- Когда пользователь вводит любое значение, кроме "да" после вопроса про желание получить информацию о символе года рождения,
  программа выполняется дальше, как если бы пользователь ввел "нет" (исправлено)


Используемые знания:
-
1. Математические операторы
2. Логические операторы
3. Объявление переменных
4. Оператор if|elif|else
5. Цикл while и инструкции continue|break
6. Цикл for
7. Строки и методы строк
8. Списки (одномерные и двумерные) и методы списков
9. Обработка исключений try|except
10. Инструкции match|case
11. Импорт модулей (random и собственные)
12. Форматирование и f-строки
13. Объявление и вызов функций
14. Динамическая типизация
15. Оператор walrus
16. Функция вывода print()
17. Функция ввода input()
18. Методы модуля random


Модули программы
-
1. Вопрос пользователю, знает ли он свой знак зодиака.
2. Запрос даты рождения у пользователя.
3. Определение знака зодиака по введенной дате рождения.
4. Определение стихии знака зодиака.
5. Выдача предсказания по знаку зодиака.
6. Описание знака зодиака.
7. Рандомный дефолтный текст.
8. Пасхалка.
9. Вопрос пользователю, хочет ли он узнать свой символ по году рождения.
10. Ввод года рождения.
11. Определение по году рождения символа.
12. Вопрос пользователю, хочет ли он еще раз получить предскзание.




Тестирование модулей
-

Чек-лист "Запрос даты рождения у пользователя"
- Проверить граничные значения
- Проверить соответствие ЗЗ дате