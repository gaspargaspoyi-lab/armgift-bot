from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

TOKEN = '8788241993:AAFx4mK3B-nDF9mNlfaru_hUMkq_j6NC5KM'
CARD_DETAILS = "💳 Реквизиты для оплаты:\n\nНомер карты: 1234 5678 1234 5678\nБанк: Тинькофф (Иван И.)\n\nПожалуйста, после перевода пришлите скриншот!"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- КНОПКИ ---

# Главное меню
main_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎁 Купить подарок", callback_data="buy_gift")],
    [InlineKeyboardButton(text="ℹ️ Подробнее", callback_data="info")]
])

# Разделы подарков
gift_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="15⭐️ (Мишка, Сердце)", callback_data="prod_15")],
    [InlineKeyboardButton(text="25⭐️ (Подарок, Роза)", callback_data="prod_25")],
    [InlineKeyboardButton(text="50⭐️ (Торт, Букет, Ракета)", callback_data="prod_50")],
    [InlineKeyboardButton(text="100⭐️ (Кубик, Кольцо, Бриллиант)", callback_data="prod_100")]
])

# --- ОБРАБОТЧИКИ ---

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет! Я бот для покупки Telegram Stars.\n"
        "🕒 Часы работы: 11:00 - 22:00.\n\n"
        "Нажми кнопку ниже, чтобы узнать больше или перейти к покупке.", 
        reply_markup=main_kb
    )

@dp.callback_query(F.data == "info")
async def info(callback: types.CallbackQuery):
    text = (
        "Привет! Я твой персональный помощник по покупке Telegram Stars.\n\n"
        "🕒 Часы работы магазина: с 11:00 до 22:00.\n\n"
        "⚠️ Если вы оформили заказ в нерабочее время, пожалуйста, дождитесь открытия магазина. "
        "Ваш заказ обязательно будет обработан сразу после нашего открытия. "
        "Спасибо за терпение и понимание! ♥️"
    )
    await callback.message.answer(text)

@dp.callback_query(F.data == "buy_gift")
async def buy_stars(callback: types.CallbackQuery):
    await callback.message.answer("Выберите нужный вам набор подарков:", reply_markup=gift_kb)

@dp.callback_query(F.data.startswith("prod_"))
async def process_buy(callback: types.CallbackQuery):
    # Добавляем реквизиты после выбора
    await callback.message.answer(f"Отличный выбор!\n\n{CARD_DETAILS}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
