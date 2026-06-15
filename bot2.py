# import telebot
# from telebot import types
# bot = telebot.TeleBot("8839353771:AAHHGBZXjA8MZ-OuJos8lSK0dY3ML2FgesM")
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("Меню")
#     btn2 = types.KeyboardButton("Время")
#     btn3 = types.KeyboardButton("Адреса")
#     markup.add(btn1, btn2 , btn3 )
#     bot.send_message(message.chat.id, "выбери одну кнопку: ", reply_markup=markup )
#
#
#
#
# @bot.message_handler(func=lambda message: True)
# def handler_message(message):
#     if message.text == "Меню":
#         bot.send_message(message.chat.id, "Dune 2", "")
#     elif message.text=="Информация про курсы":
#         bot.send_message(message.chat.id, "В Okurmen kids есть куосы про фронтенд разработке, " "\n по бекенд разработке и по разработке игр")
#     elif message.text=="Адреса и контакты":
#         markup = types.ReplyKeyboardMarkup(row_width=2)
#         btn1 = types.InlineKeyboardButton("Адреса,", url="https://2gis.kg/bishkek/firm/70000001093515114")
#         btn2 = types.InlineKeyboardButton("Инстагарм,", url="https://www.instagram.com/okurmen_kids/")
#         btn3 = types.InlineKeyboardButton("Сайт,", url="https://www.okurmen.com/")
#         markup.add(btn1, btn2 , btn3 )
#         bot.send_message(message.chat.id, "Выберите одну кнопку: ", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, "Выберите кнопку")
#
# bot.polling(non_stop=True)
# #
# #
#
# #
# # import telebot
# # from telebot import types
# #
# # bot = telebot.TeleBot("8568285549:AAFcyu6VLWBajuOElBQKgg25molLRnnf7Qk")
# #
# #
# # @bot.message_handler(commands=['start'])
# # def start(message):
# #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# #     btn1 = types.KeyboardButton("Меню")
# #     btn2 = types.KeyboardButton("Время")
# #     btn3 = types.KeyboardButton("Адрес")
# #     markup.add(btn1, btn2, btn3)
# #     bot.send_message( message.chat.id, "Выберите кнопку:",reply_markup=markup )
# #
# #
# # @bot.message_handler(func=lambda message: True)
# # def handler_message(message):
# #     if message.text == "Меню":
# #         bot.send_message( message.chat.id,"Меню:Dune  Oppenheimer  Inside Out 2")
# #     elif message.text == "Время":
# #         bot.send_message( message.chat.id,"Время:" "Dune 2: 14:00, 19:00" "Inside Out 2: 16:30, 21:00" "Oppenheimer Inside Out 2: 10:30, 13:30")
# #     elif message.text == "Адрес":
# #         markup = types.InlineKeyboardMarkup()
# #         btn1 = types.InlineKeyboardButton("Адрес",  url="https://2gis.kg/bishkek/search/%D0%AE%D0%BD%D1%83%D1%81%D0%B0%D0%BB%D0%B8%D0%B5%D0%B2%D0%B0%2040%D0%B0%20Cosmopark")
# #         btn2 = types.InlineKeyboardButton("Сайт",  url="https://cosmopark.kg?utm_source=chatgpt.com")
# #         markup.add(btn1, btn2)
# #         bot.send_message(message.chat.id, "Адрес:\nг. Бишкек, ул. Юнусалиева, 40А",reply_markup=markup)
# #     else:
# #         bot.send_message(message.chat.id, "Выберите кино ")
# # bot.polling(non_stop=True)
#
#
# #
# #
#
#
# # import telebot
# # from telebot import types
# #
# # bot = telebot.TeleBot("8568285549:AAFcyu6VLWBajuOElBQKgg25molLRnnf7Qk")
# #
# # @bot.message_handler(commands=['start'])
# # def start(message):
# #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# #
# #     btn1 = types.KeyboardButton("Эйфель мунарасы")
# #     btn2 = types.KeyboardButton("Бурж-Халифа")
# #     btn3 = types.KeyboardButton("Кытай дубалы")
# #
# #     markup.add(btn1, btn2, btn3)
# #
# #     bot.send_message(
# #         message.chat.id,
# #         "Выберите одну фото или кнопку:",
# #         reply_markup=markup
# #     )
# #
# # @bot.message_handler(func=lambda message: True)
# # def places(message):
# #
# #     if message.text == "Эйфель мунарасы":
# #
# #         bot.send_photo(
# #             message.chat.id,
# #             "https://upload.wikimedia.org/wikipedia/commons/a/a8/Tour_Eiffel_Wikimedia_Commons.jpg",
# #             "Эйфель мунарасы — Париждин символу. 1889-жылы курулган."
# #         )
# #
# #         markup = types.InlineKeyboardMarkup()
# #         btn = types.InlineKeyboardButton(
# #             "Картадан ачуу",
# #             url="https://maps.google.com/?q=Eiffel+Tower"
# #         )
# #         markup.add(btn)
# #
# #         bot.send_message(message.chat.id, "Карта:", reply_markup=markup)
# #
# #     elif message.text == "Бурж-Халифа":
# #
# #         bot.send_photo(
# #             message.chat.id,
# #             "https://upload.wikimedia.org/wikipedia/commons/9/93/Burj_Khalifa.jpg",
# #             "Бурж-Халифа — дүйнөдөгү эң бийик имарат. Дубай шаарында жайгашкан."
# #         )
# #
# #         markup = types.InlineKeyboardMarkup()
# #         btn = types.InlineKeyboardButton(
# #             "Картадан ачуу",
# #             url="https://maps.google.com/?q=Burj+Khalifa"
# #         )
# #         markup.add(btn)
# #
# #         bot.send_message(message.chat.id, "Карта:", reply_markup=markup)
# #
# #     elif message.text == "Кытай дубалы":
# #
# #         bot.send_photo(
# #             message.chat.id,
# #             "https://upload.wikimedia.org/wikipedia/commons/1/10/20190501114940%21Great_Wall_of_China_Mutianyu.jpg",
# #             "Кытай дубалы — дүйнөдөгү эң узун коргон дубал."
# #         )
# #
# #         markup = types.InlineKeyboardMarkup()
# #         btn1 = types.InlineKeyboardButton(
# #             "Картадан ачуу",
# #             url="https://maps.google.com/?q=Great+Wall+of+China"
# #         )
# #         markup.add(btn1)
# #
# #         bot.send_message(message.chat.id, "Карта:", reply_markup=markup)
# #
# #     else:
# #         bot.send_message(message.chat.id, "Төмөнкү кнопкалардын бирин басыңыз.")
# #
# # bot.polling(non_stop=True)


import telebot
from telebot import types

TOKEN = "8896853586:AAGMLv1h3p9JCHMPYP0nwHDB7yqD8QdN_10"
GROUP_ID = -1003961108035

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("📚 Курска жазылуу")
    kb.add("📖 Курстар тууралуу", "📅 Расписание")
    kb.add("💸 Оплата", "🔔 Напоминания")
    kb.add("📞 Байланыш")

    bot.send_message(
        message.chat.id,
        "Салам! Окурмен борборуна кош келиңиз 📚\n\nЭмне кылгыңыз келет?",
        reply_markup=kb
    )


@bot.message_handler(func=lambda m: True)
def menu(message):
    text = message.text

    if text == "📖 Курстар тууралуу":
        bot.send_message(
            message.chat.id,
            "📝 IT / Программалоо курсу — 5 ай\n\n"
            "💵 Ай сайын: 12 000 сом\n"
            "💰 Толук төлөм: 60 000 сом\n\n"
            "Курстун ичинде:\n"
            "✅ IT / Программалоо\n"
            "✅ Англис тили\n"
            "✅ Жеке өнүгүү\n"
            "✅ Сертификат"
        )

    elif text == "📅 Расписание":
        bot.send_message(
            message.chat.id,
            "🗓 Бул жуманын графиги\n\n"
            "вт 8:30 — IT\n"
            "ср 9:00 — English\n"
            "чт 8:30 — IT\n"
            "пт 9:00 — English\n"
            "сб 8:30 — IT\n"
            "вс 10:00 — Жеке өнүгүү\n\n"
            "📍 Табышалиева көчөсү, 29"
        )

    elif text == "💸 Оплата":
        bot.send_message(
            message.chat.id,
            "💳 Төлөм\n\n"
            "1 ай — 12 000 сом\n"
            "5 ай — 60 000 сом\n\n"
            "Төлөгөндөн кийин скриншот жөнөтүңүз."
        )

    elif text == "🔔 Напоминания":
        bot.send_message(
            message.chat.id,
            "🔔 Эскертме күйгүзүлдү."
        )

    elif text == "📞 Байланыш":
        bot.send_message(
            message.chat.id,
            "📍 Дарек: Табышалиева көчөсү, 29\n"
            "📞 Телефон: +996 \n"
            "👤 Менеджер: @Khaddizh_manager"
        )

    elif text == "📚 Курска жазылуу":
        msg = bot.send_message(
            message.chat.id,
            "Аты-жөнүңүздү жана телефон номериңизди жазыңыз.\n"
            "Мисалы: Азирет 0555123456"
        )
        bot.register_next_step_handler(msg, registration)

    else:
        bot.send_message(
            message.chat.id,
            "Негизги меню үчүн /start басыңыз."
        )

def registration(message):
    if not message.text:
        msg = bot.send_message(message.chat.id, "Сураныч, текст түрүндө (Атыңызды жана номериңизди) жазыңыз:")
        bot.register_next_step_handler(msg, registration)
        return

    data = message.text
    username = f"@{message.from_user.username}" if message.from_user.username else "Жок"


    bot.send_message(
        GROUP_ID,
        f"🔔 Жаңы жазылуу:\n"
        f"📝 Маалымат: {data}\n"
        f"🆔 Telegram ID: {message.chat.id}\n"
        f"👤 Юзернейм: {username}"
    )


    bot.send_message(
        message.chat.id,
        "🎉 Сиз ийгиликтүү катталдыңыз! Менеджер сиз менен тез арада байланышат."
    )


bot.polling(none_stop=True)

