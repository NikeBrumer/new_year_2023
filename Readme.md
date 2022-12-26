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
- Если слово с опечаткой или другое - повторный ввод (импрув: добавить слово по маске и уточнение)
- Добавлены прилагательные к знаку зодиака
- Определена стихия
- Пасхалка: Змееносец
- Тексты обращения составляются рандомно для разнообразия
- Для каждого ЗЗ свое предсказание, сделанное заранее
- красивое оформление в консоли
- Определение животного-символа по году рождения
- Запрос на повторное предсказание
  """
  24.12.2022: На данный момент в программе написан такой функционал:
- вопрос пользователю, знает ли он свой знак зодиака;
  - если да: просьба ввести свой знак зодиака;
  - если нет: определение знака зодиака по дате рождения;
- проверка валидности ответа да/нет;
  - если введено "да" или "нет" в любом регистре - программа выполняется дальше;
  - если введено что-то иное - просьба ввести еще раз до тех пор, пока программа не получит валидный ответ;
- проверка валидности введенного знака зодиака:
    - если валидно, то запись ответа в переменную zodiac;
    - если невалидно, то просьба ввести валидный ответ циклично;
- список дефолтного повествования и рандомный выбор по диапазонам;
- проверка валидности введенной даты рождения:
  - если валидно, то запись в переменную zodiac;
  - если не валидно, то просьба ввести валидную дату рождения



  Что нужно сделать:
- создать списки и функцию с непосредственными предсказаниями;
- создать списки и функцию с прилагательными;
- создать список и функцию со стихиями;
- написать формирование текста вывода: дефолтный текст + знак зодиака + стихия +
  прилагательные + предсказание;
- вопрос пользователю, хочет ли он сделать предсказание еще кому-нибудь или достаточно;
- пасхалка про змееносца;
- вопрос пользователю, хочет ли он узнать животное-символ года + ввод года рождения; (+можно указать возраст, но это доп функция, т.к. надо высчитать с текущей датой, что сложно без функции даты, которую не проходила)


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