"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
user_age = None
while user_age is None:
  input_value = input('Введите пожалуйста, Ваш возраст: ')
  try:
    user_age = int(input_value)
  except ValueError:
     print('{input} - Это не число, пожалуйста введите только число'.format(input=input_value))

def main(age):
      if age <= 6: 
        return 'Детский сад'
      elif age <= 17:
        return 'Школа'
      elif age <= 24:
        return 'ВУЗ'
      else:
        return 'Работа'
res = main(user_age)
print(res)
