"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
  answer = 'Хорошо'
  ask = ''
  try:
    while ask != answer:
      ask = input('Как дела? \n-')  
      print(ask)
  except KeyboardInterrupt:
    print('Пока')

hello_user()

