from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db

users_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Бизнинг Каталог 📒")],
        [KeyboardButton("Боғланиш ☎️")],
        [KeyboardButton("Ижтимоий тармоқларимиз 📱")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
