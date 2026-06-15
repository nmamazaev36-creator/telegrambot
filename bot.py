# import telebot
#
#
# token="8715665917:AAHbN6rEBxWEG66KFQgL2dlQDoFaOrAEpsQ"
#
# bot = telebot.TeleBot(token)
#
#
# @bot.message_handler(commands=["start"])
# def hello_(message):
#     bot.send_message(message.chat.id, "Привет, я твой бот ""первый телеграм-бот")
#
# @bot.message_handler(commands=["start"])
# def hello_(message):
#     bot.send_message(message.chat.id, "Напиши мне любое сообщениеб""и я попробую ответить на него")
#
#
#
# @bot.message_handler(content_types=["text"])
# def reply(message):
#     if message.text=="Привет":
#         bot.reply_to(message, "Как дела")
#     elif message.text=="Как тебя зовут?":
#         bot.reply_to(message, f"Меня зовут {bot.get_me().first_name}")
#     else:
#         bot.reply_to(message, message.text)
#
#
# bot.polling()
from _pyrepl import commands

# import telebot
#
#
# token="8839353771:AAHHGBZXjA8MZ-OuJos8lSK0dY3ML2FgesM"
#
# bot = telebot.TeleBot(token)
#
#
# @bot.message_handler(commands=["start"])
# def hello_(message):
#     bot.send_message(message.chat.id, "Это кинотеатр Манас")
#
# @bot.message_handler(commands=["about"])
# def hello_(message):
#     bot.send_message(message.chat.id, "Манас кинотеатр построен в 2023-год  там 50 разный кино и мультфильмы ")
#
#
#
# @bot.message_handler(commands=[""])
# def reply(message):
#     bot.send_message(message.chat.id, "Кызыл-Койнокчон 2  время 20:00 до 23:00")
#
# bot.polling()

import telebot

TOKEN = "8568285549:AAFcyu6VLWBajuOElBQKgg25molLRnnf7Qk"

bot = telebot.TeleBot(TOKEN)

heroes = {
    "шрек": "Шрек живёт на болоте и любит покой! ",
    "том": "Том всю жизнь пытается поймать Джерри, но ему редко везёт! ",
    "спанч боб": "Кто живёт на дне океана? Конечно же, Спанч Боб! ",
    "джерри": "Джерри — маленькая мышка, которая постоянно обыгрывает Тома! ",
    "микки": "Микки Маус — один из самых известных мультгероев в мире! "
}

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! 🎬 Я мультяшный бот.\nНапиши имя своего любимого мультгероя!"
    )

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "Напиши имя мультгероя, и я расскажу о нём что-нибудь интересное!"
    )

@bot.message_handler(commands=["info"])
def info(message):
    username = message.from_user.username

    if username:
        username_text = f"@{username}"
    else:
        username_text = "нет username"

    bot.send_message(
        message.chat.id,
        f" Имя: {message.from_user.first_name}"
        f" Username: {username_text}"
    )

@bot.message_handler(func=lambda message: True)
def cartoon_hero(message):
    text = message.text.lower()

    if text in heroes:
        bot.send_message(message.chat.id, heroes[text])
    else:
        bot.send_message(
            message.chat.id,
            "Я не знаю такого героя, но, возможно, он классный!"
        )

bot.polling()