from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db

users_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Бизнинг Каталог 📒")

        ],
        [
            KeyboardButton("Боғланиш ☎️")
        ],
        [
            KeyboardButton("Ижтимоий тармоқларимиз 📱")
        ]
    ], resize_keyboard=True
)


exit_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('❌')
        ]
    ], resize_keyboard=True
)

send_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Contact', request_contact=True),
        ]
    ], resize_keyboard=True
)
