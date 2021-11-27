"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
questions_and_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}

def ask_user(answers_dict):
    while True:
      try:
          user_response = input('Ask a question: \n')
          print(answers_dict.get(user_response, 'Im sorry I didnt catch you'))
      except KeyboardInterrupt:
        print('Bye-Bye!')
        break

ask_user(questions_and_answers)
