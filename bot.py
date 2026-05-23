import os
from flask import Flask
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import asyncio

BOT_TOKEN = os.getenv('BOT_TOKEN')
GAME_URL = "https://graffitifers-cmd.github.io/Hot-Girls-Puzzle-Game/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running! 🤖"

@app.route('/webhook', methods=['POST'])
def webhook():
    return "OK"

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 тискай сюда", web_app=WebAppInfo(url=GAME_URL))]
    ])
    
    caption = (
        "🎉 **Добро пожаловать в Hot Girls Puzzle Game!**\n\n"
        "🧩 Собирай пазлы, зарабатывай звёзды ⭐️\n"
        "🔥 Играй прямо сейчас!\n\n"
        "Жми кнопку ниже 👇"
    )
    
    await message.answer_photo(
        photo=types.FSInputFile("welcome.jpg"),
        caption=caption,
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

async def start_bot():
    await dp.start_polling(bot)

async def main():
    # Запускаем бота и Flask вместе
    await asyncio.gather(
        start_bot(),
        asyncio.get_event_loop().run_in_executor(None, app.run)
    )

if __name__ == "__main__":
    asyncio.run(main())
