from random import choice
from func_of_project import *

# description = '(описание)'
prediction = '(предсказание)'
element = '(стихия)'

print(f'\n{choice(defolt[:3])} {questions_zodiak()}. {choice(defolt[3:6])} {description()}.\n'
      f'{choice(defolt[6:9])} {choice(defolt[9:12])} {element}. {choice(defolt[12:15])}\n'
      f'{choice(defolt[15:18])}\n{choice(defolt[18:])} {prediction}')

