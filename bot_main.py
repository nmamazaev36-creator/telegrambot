# import telebot
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# TOKEN = "8450163431:AAG7-3labitwEXgx_JByMrz8dCZEVV6WTaU"
# bot = telebot.TeleBot(TOKEN)
#
# # =================== БАЗА ДАННЫХ ===================
#
# MOVIES = [
#     {
#         "id": "movie_1",
#         "title": "Интерстеллар",
#         "year": 2014,
#         "rating": "⭐ 8.7",
#         "genre": "Фантастика / Драма",
#         "description": "Группа исследователей отправляется сквозь червоточину в поисках новой планеты. Когда Земля умирает, экипаж путешествует за пределы галактики в надежде найти новый дом.",
#         "photo": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
#         "duration": "169 мин",
#         "director": "Кристофер Нолан"
#     },
#     {
#         "id": "movie_2",
#         "title": "Начало",
#         "year": 2010,
#         "rating": "⭐ 8.8",
#         "genre": "Фантастика / Триллер",
#         "description": "Кобб — вор, крадущий секреты из подсознания во время сна. Ему предлагают внедрить идею в разум человека.",
#         "photo": "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
#         "duration": "148 мин",
#         "director": "Кристофер Нолан"
#     },
#     {
#         "id": "movie_3",
#         "title": "Матрица",
#         "year": 1999,
#         "rating": "⭐ 8.7",
#         "genre": "Фантастика / Экшн",
#         "description": "Хакер Нео узнаёт, что его мир — симуляция машин. Он присоединяется к повстанцам, чтобы освободить человечество.",
#         "photo": "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
#         "duration": "136 мин",
#         "director": "Братья Вачовски"
#     },
#     {
#         "id": "movie_4",
#         "title": "Мстители: Финал",
#         "year": 2019,
#         "rating": "⭐ 8.4",
#         "genre": "Фантастика / Экшн",
#         "description": "Выжившие супергерои собираются, чтобы обратить вред, причинённый Таносом.",
#         "photo": "https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg",
#         "duration": "181 мин",
#         "director": "Братья Руссо"
#     },
#     {
#         "id": "movie_5",
#         "title": "Паразиты",
#         "year": 2019,
#         "rating": "⭐ 8.5",
#         "genre": "Триллер / Драма",
#         "description": "Малоимущая семья внедряется в жизнь богатой семьи. Но их план рушится, когда вскрываются тёмные секреты дома.",
#         "photo": "https://upload.wikimedia.org/wikipedia/en/5/53/Parasite_%282019_film%29.png",
#         "duration": "132 мин",
#         "director": "Пон Джун-хо"
#     },
# ]
#
# SERIES = [
#     {
#         "id": "series_1",
#         "title": "Breaking Bad",
#         "year": "2008–2013",
#         "rating": "⭐ 9.5",
#         "genre": "Драма / Триллер",
#         "description": "Учитель химии начинает варить метамфетамин и постепенно превращается в безжалостного преступника.",
#         "photo": "https://upload.wikimedia.org/wikipedia/en/6/61/Breaking_Bad_title_card.png",
#         "seasons": "5 сезонов",
#         "episodes": "62 эпизода"
#     },
#     {
#         "id": "series_2",
#         "title": "Игра Престолов",
#         "year": "2011–2019",
#         "rating": "⭐ 9.2",
#         "genre": "Фэнтези / Драма",
#         "description": "Великие дома борются за Железный Трон, пока с севера надвигается древняя угроза.",
#         "photo": "https://upload.wikimedia.org/wikipedia/en/d/d8/Game_of_Thrones_Season_3.jpg",
#         "seasons": "8 сезонов",
#         "episodes": "73 эпизода"
#     },
#     {
#         "id": "series_3",
#         "title": "Очень странные дела",
#         "year": "2016–2025",
#         "rating": "⭐ 8.7",
#         "genre": "Ужасы / Фантастика",
#         "description": "В маленьком городке пропадает мальчик. Его друзья раскрывают тайны сверхъестественного.",
#         "photo": "https://upload.wikimedia.org/wikipedia/en/4/4e/Stranger_Things_season_1.jpg",
#         "seasons": "5 сезонов",
#         "episodes": "42 эпизода"
#     },
#     {
#         "id": "series_4",
#         "title": "Чёрное зеркало",
#         "year": "2011–наст.",
#         "rating": "⭐ 8.8",
#         "genre": "Антология / Фантастика",
#         "description": "Антологический сериал о тёмной стороне технологий. Каждый эпизод — отдельная история.",
#         "photo": "https://upload.wikimedia.org/wikipedia/en/7/76/Black_Mirror_Season_1_Cover.png",
#         "seasons": "6 сезонов",
#         "episodes": "27 эпизодов"
#     },
#     {
#         "id": "series_5",
#         "title": "Ведьмак",
#         "year": "2019–2023",
#         "rating": "⭐ 8.1",
#         "genre": "Фэнтези / Экшн",
#         "description": "Геральт из Ривии — охотник на монстров — борется за место в мире, где люди опаснее чудовищ.",
#         "photo": "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Witcher_Season_1_Poster.jpg",
#         "seasons": "3 сезона",
#         "episodes": "24 эпизода"
#     },
# ]
#
# HORRORS = [
#     {
#         "id": "horror_1",
#         "title": "Оно",
#         "year": 2017,
#         "rating": "⭐ 7.3",
#         "genre": "Ужасы / Триллер",
#         "description": "Группа детей сталкивается с клоуном Пеннивайзом, который охотится на детей каждые 27 лет.",
#         "photo": "https://upload.wikimedia.org/wikipedia/en/5/5c/It_%282017%29_poster.jpg",
#         "scare_level": "👻👻👻👻",
#         "director": "Андрес Мускетти"
#     },
#     {
#         "id": "horror_2",
#         "title": "Реинкарнация",
#         "year": 2018,
#         "rating": "⭐ 7.3",
#         "genre": "Мистика / Ужасы",
#         "description": "После смерти бабушки семья раскрывает ужасающие тайны своего рода.",
#         "photo": "https://upload.wikimedia.org/wikipedia/en/a/a8/Hereditary_film_poster.png",
#         "scare_level": "👻👻👻👻👻",
#         "director": "Ари Астер"
#     },
#     {
#         "id": "horror_3",
#         "title": "Тихое место",
#         "year": 2018,
#         "rating": "⭐ 7.5",
#         "genre": "Ужасы / Триллер",
#         "description": "Семья выживает в мире, где монстры охотятся на звук. Малейший шум означает смерть.",
#         "photo": "https://upload.wikimedia.org/wikipedia/en/8/87/A_Quiet_Place_film_poster.jpg",
#         "scare_level": "👻👻👻👻",
#         "director": "Джон Красински"
#     },
#     {
#         "id": "horror_4",
#         "title": "Прочь",
#         "year": 2017,
#         "rating": "⭐ 7.7",
#         "genre": "Ужасы / Триллер",
#         "description": "Молодой человек знакомится с семьёй подруги и замечает всё более странное поведение окружающих.",
#         "photo": "https://upload.wikimedia.org/wikipedia/en/a/a1/Get_Out_poster.png",
#         "scare_level": "👻👻👻👻",
#         "director": "Джордан Пил"
#     },
#     {
#         "id": "horror_5",
#         "title": "Астрал",
#         "year": 2010,
#         "rating": "⭐ 7.2",
#         "genre": "Ужасы / Мистика",
#         "description": "Душа сына застряла в тёмном измерении, полном злых духов.",
#         "photo": "https://upload.wikimedia.org/wikipedia/en/4/48/Insidious_Poster.jpg",
#         "scare_level": "👻👻👻",
#         "director": "Джеймс Ван"
#     },
# ]
#
# # =================== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ===================
#
# def find_item(item_id):
#     for lst in [MOVIES, SERIES, HORRORS]:
#         for item in lst:
#             if item["id"] == item_id:
#                 return item
#     return None
#
# def get_back_data(item_id):
#     if item_id.startswith("movie"):   return "category_movies"
#     if item_id.startswith("series"):  return "category_series"
#     if item_id.startswith("horror"):  return "category_horrors"
#     return "main_menu"
#
# def build_caption(item):
#     item_id = item["id"]
#     if item_id.startswith("movie"):
#         return (
#             f"🎬 *{item['title']}* ({item['year']})\n\n"
#             f"🎭 Жанр: {item['genre']}\n"
#             f"⏱ Длительность: {item['duration']}\n"
#             f"🎥 Режиссёр: {item['director']}\n"
#             f"{item['rating']}\n\n"
#             f"📖 *Описание:*\n{item['description']}"
#         )
#     elif item_id.startswith("series"):
#         return (
#             f"📺 *{item['title']}* ({item['year']})\n\n"
#             f"🎭 Жанр: {item['genre']}\n"
#             f"🗂 Сезонов: {item['seasons']}\n"
#             f"📼 Эпизодов: {item['episodes']}\n"
#             f"{item['rating']}\n\n"
#             f"📖 *Описание:*\n{item['description']}"
#         )
#     else:
#         return (
#             f"👻 *{item['title']}* ({item['year']})\n\n"
#             f"🎭 Жанр: {item['genre']}\n"
#             f"🎥 Режиссёр: {item['director']}\n"
#             f"😱 Страшность: {item['scare_level']}\n"
#             f"{item['rating']}\n\n"
#             f"📖 *Описание:*\n{item['description']}"
#         )
#
# # =================== КЛАВИАТУРЫ ===================
#
# def main_menu_kb():
#     kb = InlineKeyboardMarkup()
#     kb.add(InlineKeyboardButton("🎬 Фильмы",  callback_data="category_movies"))
#     kb.add(InlineKeyboardButton("📺 Сериалы", callback_data="category_series"))
#     kb.add(InlineKeyboardButton("👻 Хорроры", callback_data="category_horrors"))
#     return kb
#
# def list_kb(items, back_data):
#     kb = InlineKeyboardMarkup()
#     for item in items:
#         emoji = "🎬" if "movie" in item["id"] else "📺" if "series" in item["id"] else "👻"
#         kb.add(InlineKeyboardButton(
#             f"{emoji} {item['title']} ({item['year']})",
#             callback_data=f"item_{item['id']}"
#         ))
#     kb.add(InlineKeyboardButton("◀️ Назад", callback_data=back_data))
#     return kb
#
# def item_kb(back_data):
#     kb = InlineKeyboardMarkup()
#     kb.add(InlineKeyboardButton("◀️ Назад к списку", callback_data=back_data))
#     kb.add(InlineKeyboardButton("🏠 Главное меню",   callback_data="main_menu"))
#     return kb
#
# # =================== ХЕНДЛЕРЫ ===================
#
# @bot.message_handler(commands=["start"])
# def start(message):
#     bot.send_message(
#         message.chat.id,
#         "🎥 *CinemaBot* — твой кинотеатр в Telegram!\n\nВыбери категорию:",
#         parse_mode="Markdown",
#         reply_markup=main_menu_kb()
#     )
#
# @bot.callback_query_handler(func=lambda call: True)
# def handle_callback(call):
#     data = call.data
#
#     if data == "main_menu":
#         bot.edit_message_text(
#             "🎥 *CinemaBot* — твой кинотеатр в Telegram!\n\nВыбери категорию:",
#             call.message.chat.id, call.message.message_id,
#             parse_mode="Markdown", reply_markup=main_menu_kb()
#         )
#
#     elif data == "category_movies":
#         bot.edit_message_text(
#             "🎬 *Фильмы*\n\nВыбери фильм:",
#             call.message.chat.id, call.message.message_id,
#             parse_mode="Markdown", reply_markup=list_kb(MOVIES, "main_menu")
#         )
#
#     elif data == "category_series":
#         bot.edit_message_text(
#             "📺 *Сериалы*\n\nВыбери сериал:",
#             call.message.chat.id, call.message.message_id,
#             parse_mode="Markdown", reply_markup=list_kb(SERIES, "main_menu")
#         )
#
#     elif data == "category_horrors":
#         bot.edit_message_text(
#             "👻 *Хорроры*\n\nВыбери фильм ужасов:",
#             call.message.chat.id, call.message.message_id,
#             parse_mode="Markdown", reply_markup=list_kb(HORRORS, "main_menu")
#         )
#
#     elif data.startswith("item_"):
#         item_id  = data[5:]
#         item     = find_item(item_id)
#         back     = get_back_data(item_id)
#
#         if item:
#             bot.delete_message(call.message.chat.id, call.message.message_id)
#             bot.send_photo(
#                 call.message.chat.id,
#                 photo=item["photo"],
#                 caption=build_caption(item),
#                 parse_mode="Markdown",
#                 reply_markup=item_kb(back)
#             )
#
#     # Назад из карточки с фото
#     elif data in ("category_movies", "category_series", "category_horrors"):
#         if data == "category_movies":
#             text, items = "🎬 *Фильмы*\n\nВыбери фильм:", MOVIES
#         elif data == "category_series":
#             text, items = "📺 *Сериалы*\n\nВыбери сериал:", SERIES
#         else:
#             text, items = "👻 *Хорроры*\n\nВыбери фильм ужасов:", HORRORS
#
#         bot.delete_message(call.message.chat.id, call.message.message_id)
#         bot.send_message(
#             call.message.chat.id, text,
#             parse_mode="Markdown",
#             reply_markup=list_kb(items, "main_menu")
#         )
#
#     bot.answer_callback_query(call.id)
#
# # =================== ЗАПУСК ===================
#
#
# bot.infinity_polling()

from flask import Flask
from threading import Thread
import os

web = Flask('')

@web.route('/')
def home():
    return "Bot is alive"

def run_web():
    web.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

Thread(target=run_web).start()


import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = ("8450163431:AAG7-3labitwEXgx_JByMrz8dCZEVV6WTaU")
bot = telebot.TeleBot(BOT_TOKEN)
BOT_TOKEN = os.environ.get("BOT_TOKEN")



MOVIES = [
    {
        "id": "movie_1",
        "title": "Интерстеллар",
        "year": 2014,
        "rating": "⭐ 8.7",
        "genre": "Фантастика / Драма",
        "description": "Группа исследователей отправляется сквозь червоточину в поисках новой планеты. Когда Земля умирает, экипаж путешествует за пределы галактики в надежде найти новый дом.",
        "photo": "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
        "duration": "169 мин",
        "director": "Кристофер Нолан"
    },
    {
        "id": "movie_2",
        "title": "Начало",
        "year": 2010,
        "rating": "⭐ 8.8",
        "genre": "Фантастика / Триллер",
        "description": "Кобб — вор, крадущий секреты из подсознания во время сна. Ему предлагают внедрить идею в разум человека.",
        "photo": "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
        "duration": "148 мин",
        "director": "Кристофер Нолан"
    },
    {
        "id": "movie_3",
        "title": "Матрица",
        "year": 1999,
        "rating": "⭐ 8.7",
        "genre": "Фантастика / Экшн",
        "description": "Хакер Нео узнаёт, что его мир — симуляция машин. Он присоединяется к повстанцам, чтобы освободить человечество.",
        "photo": "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
        "duration": "136 мин",
        "director": "Братья Вачовски"
    },
    {
        "id": "movie_4",
        "title": "Мстители: Финал",
        "year": 2019,
        "rating": "⭐ 8.4",
        "genre": "Фантастика / Экшн",
        "description": "Выжившие супергерои собираются, чтобы обратить вред, причинённый Таносом.",
        "photo": "https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg",
        "duration": "181 мин",
        "director": "Братья Руссо"
    },
    {
        "id": "movie_5",
        "title": "Паразиты",
        "year": 2019,
        "rating": "⭐ 8.5",
        "genre": "Триллер / Драма",
        "description": "Малоимущая семья внедряется в жизнь богатой семьи. Но их план рушится, когда вскрываются тёмные секреты дома.",
        "photo": "https://upload.wikimedia.org/wikipedia/en/5/53/Parasite_%282019_film%29.png",
        "duration": "132 мин",
        "director": "Пон Джун-хо"
    },
]

SERIES = [
    {
        "id": "series_1",
        "title": "Breaking Bad",
        "year": "2008–2013",
        "rating": "⭐ 9.5",
        "genre": "Драма / Триллер",
        "description": "Учитель химии начинает варить метамфетамин и постепенно превращается в безжалостного преступника.",
        "photo": "https://upload.wikimedia.org/wikipedia/en/6/61/Breaking_Bad_title_card.png",
        "seasons": "5 сезонов",
        "episodes": "62 эпизода"
    },
    {
        "id": "series_2",
        "title": "Игра Престолов",
        "year": "2011–2019",
        "rating": "⭐ 9.2",
        "genre": "Фэнтези / Драма",
        "description": "Великие дома борются за Железный Трон, пока с севера надвигается древняя угроза.",
        "photo": "https://upload.wikimedia.org/wikipedia/en/d/d8/Game_of_Thrones_Season_3.jpg",
        "seasons": "8 сезонов",
        "episodes": "73 эпизода"
    },
    {
        "id": "series_3",
        "title": "Очень странные дела",
        "year": "2016–2025",
        "rating": "⭐ 8.7",
        "genre": "Ужасы / Фантастика",
        "description": "В маленьком городке пропадает мальчик. Его друзья раскрывают тайны сверхъестественного.",
        "photo": "https://upload.wikimedia.org/wikipedia/en/4/4e/Stranger_Things_season_1.jpg",
        "seasons": "5 сезонов",
        "episodes": "42 эпизода"
    },
    {
        "id": "series_4",
        "title": "Чёрное зеркало",
        "year": "2011–наст.",
        "rating": "⭐ 8.8",
        "genre": "Антология / Фантастика",
        "description": "Антологический сериал о тёмной стороне технологий. Каждый эпизод — отдельная история.",
        "photo": "https://upload.wikimedia.org/wikipedia/en/7/76/Black_Mirror_Season_1_Cover.png",
        "seasons": "6 сезонов",
        "episodes": "27 эпизодов"
    },
    {
        "id": "series_5",
        "title": "Ведьмак",
        "year": "2019–2023",
        "rating": "⭐ 8.1",
        "genre": "Фэнтези / Экшн",
        "description": "Геральт из Ривии — охотник на монстров — борется за место в мире, где люди опаснее чудовищ.",
        "photo": "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Witcher_Season_1_Poster.jpg",
        "seasons": "3 сезона",
        "episodes": "24 эпизода"
    },
]

HORRORS = [
    {
        "id": "horror_1",
        "title": "Оно",
        "year": 2017,
        "rating": "⭐ 7.3",
        "genre": "Ужасы / Триллер",
        "description": "Группа детей сталкивается с клоуном Пеннивайзом, который охотится на детей каждые 27 лет.",
        "photo": "https://upload.wikimedia.org/wikipedia/en/5/5c/It_%282017%29_poster.jpg",
        "scare_level": "👻👻👻👻",
        "director": "Андрес Мускетти"
    },
    {
        "id": "horror_2",
        "title": "Реинкарнация",
        "year": 2018,
        "rating": "⭐ 7.3",
        "genre": "Мистика / Ужасы",
        "description": "После смерти бабушки семья раскрывает ужасающие тайны своего рода.",
        "photo": "https://upload.wikimedia.org/wikipedia/en/a/a8/Hereditary_film_poster.png",
        "scare_level": "👻👻👻👻👻",
        "director": "Ари Астер"
    },
    {
        "id": "horror_3",
        "title": "Тихое место",
        "year": 2018,
        "rating": "⭐ 7.5",
        "genre": "Ужасы / Триллер",
        "description": "Семья выживает в мире, где монстры охотятся на звук. Малейший шум означает смерть.",
        "photo": "https://upload.wikimedia.org/wikipedia/en/8/87/A_Quiet_Place_film_poster.jpg",
        "scare_level": "👻👻👻👻",
        "director": "Джон Красински"
    },
    {
        "id": "horror_4",
        "title": "Прочь",
        "year": 2017,
        "rating": "⭐ 7.7",
        "genre": "Ужасы / Триллер",
        "description": "Молодой человек знакомится с семьёй подруги и замечает всё более странное поведение окружающих.",
        "photo": "https://m.media-amazon.com/images/M/MV5BOGIxODA4ODktZTllYS00YTU0LThkYzQtYjgyNDA2MWI5OTQ0XkEyXkFqcGc@._V1_.jpg",
        "scare_level": "👻👻👻👻",
        "director": "Джордан Пил"
    },
    {
        "id": "horror_5",
        "title": "Астрал",
        "year": 2010,
        "rating": "⭐ 7.2",
        "genre": "Ужасы / Мистика",
        "description": "Душа сына застряла в тёмном измерении, полном злых духов.",
        "photo": "https://ir.ozone.ru/s3/multimedia-0/6705984204.jpg",
        "scare_level": "👻👻👻",
        "director": "Джеймс Ван"
    },
]



def find_item(item_id):
    for lst in [MOVIES, SERIES, HORRORS]:
        for item in lst:
            if item["id"] == item_id:
                return item
    return None

def get_back_data(item_id):
    if item_id.startswith("movie"):  return "category_movies"
    if item_id.startswith("series"): return "category_series"
    if item_id.startswith("horror"): return "category_horrors"
    return "main_menu"

def build_caption(item):
    item_id = item["id"]
    if item_id.startswith("movie"):
        return (
            f"🎬 *{item['title']}* ({item['year']})\n\n"
            f"🎭 Жанр: {item['genre']}\n"
            f"⏱ Длительность: {item['duration']}\n"
            f"🎥 Режиссёр: {item['director']}\n"
            f"{item['rating']}\n\n"
            f"📖 *Описание:*\n{item['description']}"
        )
    elif item_id.startswith("series"):
        return (
            f"📺 *{item['title']}* ({item['year']})\n\n"
            f"🎭 Жанр: {item['genre']}\n"
            f"🗂 Сезонов: {item['seasons']}\n"
            f"📼 Эпизодов: {item['episodes']}\n"
            f"{item['rating']}\n\n"
            f"📖 *Описание:*\n{item['description']}"
        )
    else:
        return (
            f"👻 *{item['title']}* ({item['year']})\n\n"
            f"🎭 Жанр: {item['genre']}\n"
            f"🎥 Режиссёр: {item['director']}\n"
            f"😱 Страшность: {item['scare_level']}\n"
            f"{item['rating']}\n\n"
            f"📖 *Описание:*\n{item['description']}"
        )

# =================== КЛАВИАТУРЫ ===================

def main_menu_kb():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🎬 Фильмы",  callback_data="category_movies"))
    kb.add(InlineKeyboardButton("📺 Сериалы", callback_data="category_series"))
    kb.add(InlineKeyboardButton("👻 Хорроры", callback_data="category_horrors"))
    return kb

def list_kb(items, back_data):
    kb = InlineKeyboardMarkup()
    for item in items:
        emoji = "🎬" if "movie" in item["id"] else "📺" if "series" in item["id"] else "👻"
        kb.add(InlineKeyboardButton(
            f"{emoji} {item['title']} ({item['year']})",
            callback_data=f"item_{item['id']}"
        ))
    kb.add(InlineKeyboardButton("◀️ Назад", callback_data=back_data))
    return kb

def item_kb(back_data):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("◀️ Назад к списку", callback_data=back_data))
    kb.add(InlineKeyboardButton("🏠 Главное меню",   callback_data="main_menu"))
    return kb



@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🎥 *CinemaBot* — твой кинотеатр в Telegram!\n\nВыбери категорию:",
        parse_mode="Markdown",
        reply_markup=main_menu_kb()
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    data = call.data

    if data == "main_menu":
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
        bot.send_message(
            call.message.chat.id,
            "🎥 *CinemaBot* — твой кинотеатр в Telegram!\n\nВыбери категорию:",
            parse_mode="Markdown",
            reply_markup=main_menu_kb()
        )

    elif data == "category_movies":
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
        bot.send_message(
            call.message.chat.id,
            "🎬 *Фильмы*\n\nВыбери фильм:",
            parse_mode="Markdown",
            reply_markup=list_kb(MOVIES, "main_menu")
        )

    elif data == "category_series":
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
        bot.send_message(
            call.message.chat.id,
            "📺 *Сериалы*\n\nВыбери сериал:",
            parse_mode="Markdown",
            reply_markup=list_kb(SERIES, "main_menu")
        )

    elif data == "category_horrors":
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
        bot.send_message(
            call.message.chat.id,
            "👻 *Хорроры*\n\nВыбери фильм ужасов:",
            parse_mode="Markdown",
            reply_markup=list_kb(HORRORS, "main_menu")
        )

    elif data.startswith("item_"):
        item_id = data[5:]
        item    = find_item(item_id)
        back    = get_back_data(item_id)

        if item:
            try:
                bot.delete_message(call.message.chat.id, call.message.message_id)
            except:
                pass
            bot.send_photo(
                call.message.chat.id,
                photo=item["photo"],
                caption=build_caption(item),
                parse_mode="Markdown",
                reply_markup=item_kb(back)
            )

    bot.answer_callback_query(call.id)

# =================== ЗАПУСК ===================

print("✅ Бот запущен!")
bot.infinity_polling()