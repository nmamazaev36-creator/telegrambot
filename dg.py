# import pygame
# import random
#
# pygame.init()
#
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Лови монеты")
#
# WHITE = (255, 255, 255)
# BLUE = (0, 100, 255)
# GOLD = (255, 215, 0)
# BLACK = (0, 0, 0)
#
# player = pygame.Rect(350, 500, 50, 50)
# player_speed = 7
# player_hp = 5
#
# coin = pygame.Rect(random.randint(0, 760), 0, 40, 40)
# coin_speed = 5
#
# score = 0
# level = 0
#
#
#
# font = pygame.font.SysFont(None, 40)
#
# clock = pygame.time.Clock()
#
# running = True
# while running:
#     clock.tick(60)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     keys = pygame.key.get_pressed()
#
#     if keys[pygame.K_LEFT]:
#         player.x -= player_speed
#     if keys[pygame.K_RIGHT]:
#         player.x += player_speed
#
#     if player.left < 0:
#         player.left = 0
#     if player.right > WIDTH:
#         player.right = WIDTH
#
#     coin.y += coin_speed
#
#     if coin.y > HEIGHT:
#         coin.x = random.randint(0, 760)
#         coin.y = 0
#
#     if player.colliderect(coin):
#         score += 1
#         coin.x = random.randint(0, 760)
#         coin.y = 0
#
#     screen.fill(BLACK)
#
#     pygame.draw.rect(screen, BLUE, player)
#     pygame.draw.circle(screen, GOLD, coin.center, 20)
#
#     score_text = font.render(f"Очки: {score}", True, WHITE)
#     level.text = font.render(f"level: {level}", True, WHITE)
#     screen.blit(score_text, (10, 10))
#
#     pygame.display.flip()
#
# pygame.quit()


from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8568285549:AAFcyu6VLWBajuOElBQKgg25molLRnnf7Qk"

SIGHTS = {
    "burana": {
        "name": "Башня Бурана",
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Burana_tower.jpg/800px-Burana_tower.jpg",
        "description": (
            "🏰 *Башня Бурана*\n\n"
            "Минарет XI века в Чуйской долине — один из символов Кыргызстана. "
            "Сохранившаяся высота около 24 м. Рядом расположено поле с каменными балбалами (изваяниями). "
            "Включена в список Всемирного наследия ЮНЕСКО.\n\n"
            "📍 _Чуйская область, ~80 км от Бишкека_"
        ),
        "map_url": "https://maps.google.com/?q=42.7408,75.2589",
    },
    "panfilov": {
        "name": "Парк Панфилова",
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Bishkek_Panfilov_Park.jpg/800px-Bishkek_Panfilov_Park.jpg",
        "description": (
            "🌳 *Парк Панфилова*\n\n"
            "Центральный парк Бишкека, названный в честь генерала Ивана Панфилова. "
            "Любимое место отдыха горожан: красивые аллеи, фонтаны, аттракционы и кафе. "
            "Здесь проходят городские праздники и концерты.\n\n"
            "📍 _Бишкек, центр города_"
        ),
        "map_url": "https://maps.google.com/?q=42.8746,74.5984",
    },
    "museum": {
        "name": "Исторический музей",
        "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Kyrgyzstan_State_Historical_Museum.jpg/800px-Kyrgyzstan_State_Historical_Museum.jpg",
        "description": (
            "🏛️ *Государственный исторический музей*\n\n"
            "Главный музей Кыргызстана, расположенный на площади Ала-Тоо в Бишкеке. "
            "Хранит более 90 000 экспонатов: от древних петроглифов до предметов советской эпохи. "
            "Обязателен к посещению для всех, кто интересуется историей страны.\n\n"
            "📍 _Бишкек, площадь Ала-Тоо_"
        ),
        "map_url": "https://maps.google.com/?q=42.8715,74.5930",
    },
}


def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏰 Башня Бурана", callback_data="burana")],
        [InlineKeyboardButton("🌳 Парк Панфилова", callback_data="panfilov")],
        [InlineKeyboardButton("🏛️ Исторический музей", callback_data="museum")],
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я гид по достопримечательностям Кыргызстана.\n\n"
        "Выберите место, о котором хотите узнать:",
        reply_markup=main_menu_keyboard(),
    )


async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    key = query.data
    if key not in SIGHTS:
        return

    sight = SIGHTS[key]

    map_keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🗺️ Открыть на карте", url=sight["map_url"])],
        [InlineKeyboardButton("◀️ Назад к меню", callback_data="back")],
    ])

    try:
        await query.message.reply_photo(
            photo=sight["photo"],
            caption=sight["description"],
            parse_mode="Markdown",
            reply_markup=map_keyboard,
        )
    except Exception:
        # Если фото недоступно — отправляем только текст
        await query.message.reply_text(
            sight["description"],
            parse_mode="Markdown",
            reply_markup=map_keyboard,
        )


async def handle_back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        "Выберите достопримечательность:",
        reply_markup=main_menu_keyboard(),
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_back, pattern="^back$"))
    app.add_handler(CallbackQueryHandler(handle_button))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()