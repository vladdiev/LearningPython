"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

def hello_user():
  answer = 'Хорошо'
  ask = ''
  while ask != answer:
    ask = input('Как дела? \n-')  
    print(ask)

hello_user()