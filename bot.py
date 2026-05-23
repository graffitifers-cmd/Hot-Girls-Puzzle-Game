import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Твой токен от BotFather
BOT_TOKEN = "8644263805:AAE87Cb90KOGtcWbtLnNrJOR1tLE2V-6ZFQ"

# Ссылка на твою игру
GAME_URL = "https://graffitifers-cmd.github.io/Hot-Girls-Puzzle-Game/"

# Ссылка на картинку (загрузи её куда-то или положи рядом с ботом)
# Пока используем заглушку, потом заменишь на свою
PHOTO_URL = "https://i.imgur.com/your_image.jpg" 

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    # Кнопка "Launch Web App"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 тискай сюда", web_app=WebAppInfo(url=GAME_URL))]
    ])
    
    # Текст приветствия
    caption = (
        "🎉 **Добро пожаловать в Hot Girls Puzzle Game!**\n\n"
        "🧩 Собирай пазлы, зарабатывай звёзды ⭐️\n"
        "🔥 Горячие девочки уже ждут тебя!\n\n"
        "Нажми кнопку ниже, чтобы начать 👇"
    )
    
    # Отправляем фото с кнопкой
    # Если картинки нет, раскомментируй строку ниже и закомментируй send_photo
    # await message.answer(caption, reply_markup=keyboard, parse_mode="Markdown")
    
    await message.answer_photo(
        photo=types.FSInputFile("welcome.jpg"), # Или URL: photo="https://..."
        caption=caption,
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())