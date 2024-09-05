from aiogram.fsm.state import StatesGroup, State


class Register(StatesGroup):
    login = State()
    password = State()
