"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import datetime
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def get_planet(update, context):
  user_text = update.message.text
  selected_planet = user_text.split()[1]
  planet_list = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
  if selected_planet in planet_list:
    compute = getattr(ephem, selected_planet)(datetime.datetime.today())
    text = ephem.constellation(compute)
  else:
    text = 'Нет такой планеты'
  update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text()


def main():
    mybot = Updater({settings.API_KEY}, request_kwargs= PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start",  greet_user))
    dp.add_handler(CommandHandler("planet",  get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
