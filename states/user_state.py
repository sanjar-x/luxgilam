from aiogram.dispatcher.filters.state import State, StatesGroup

class BoglanishState(StatesGroup):
    phone = State()


class BoshqaRazmer(StatesGroup):
    boyi = State()
    eni = State()

class MuddatBoglanish(StatesGroup):
    phone = State()
