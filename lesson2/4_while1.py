"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

def hello_user():
  while True:
    answer = input('Как дела ? \n')
    if answer == 'Хорошо' or answer == 'хорошо':
      break
  
  hello_user()