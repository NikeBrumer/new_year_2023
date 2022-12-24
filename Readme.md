Программа "Предсказание на 2023"
-

(Данный проект включает в себя все изученные темы в 2022 и является итоговым на момент текущего года)

24.12.2022: На данный момент в программе написан такой функционал:
- вопрос пользователю, знает ли он свой знак зодиака;
  - если да: просьба ввести свой знак зодиака;
  - если нет: определение знака зодиака по дате рождения;
- проверка валидности ответа да/нет;
  - если введено "да" или "нет" в любом регистре - программа выполняется дальше;
  - если введено что-то иное - просьба ввести еще раз до тех пор, пока программа не получит валидный ответ;
- проверка валидности введенного знака зодиака:
    - если валидно, то запись ответа в переменную zodiak;
    - если невалидно, то просьба ввести валидный ответ циклично;
- список дефолтного повествования и рандомный выбор по диапазонам;

Что нужно сделать:
- создать списки и функцию с непосредственными предсказаниями;
- создать списки и функцию с прилагательными;
- создать список и функцию со стихиями;
- написать формирование текста вывода: дефолтный текст + знак зодиака + стихия +
прилагательные + предсказание;
- вопрос пользователю, хочет ли он сделать предсказание еще кому-нибудь или достаточно;
- пасхалка про змееносца;




Программа "Предсказание 2023 для знаков зодиака" (первое ТЗ).
-
Как работает программа:
1. Пользователь вводит знак зодиака, если знает его.
2. Если не знает, вводит день рождения (в формате "5 января")
3. Программа выводит текст с предсказанием.
Фичи:
- Если слово с опечаткой или другое - повторный ввод (импрув: добавить слово по маске и уточнение)
- Добавлены прилагательные к знаку зодиака
- Определена стихия
- Пасхалка: Змееносец
- Тексты обращения составляются рандомно для разнообразия
- Для каждого ЗЗ свое предсказание, сделанное заранее
- красивое оформление в консоли
"""