from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
import asyncio

# Твой токен, который ты получил у @BotFather
TOKEN = '8788241993:AAFx4mK3B-nDF9mNlfaru_hUMkq_j6NC5KM'

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    # Создаем кнопку, которая открывает твой index.html
    # Внимание: здесь нужно будет указать URL, когда зальем на хостинг
    web_app_url = "https://твое-имя.pythonanywhere.com" 
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть ArmGift", web_app=WebAppInfo(url=web_app_url))]
    ])
    
    await message.answer("Привет! Нажми на кнопку ниже, чтобы запустить ArmGift:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())