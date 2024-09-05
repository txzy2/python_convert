from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import app.states._reg_state as st

reg = Router()

# TODO: Разобраться с удалением сообщений


@reg.callback_query(F.data == "go")
async def start_handler(callback: CallbackQuery, state: FSMContext) -> str:
    await state.set_state(st.Register.login)
    await callback.message.answer("Введи логин")


@reg.message(st.Register.login)
async def login_handler(message: Message, state: FSMContext) -> str:
    await state.update_data(login=message.text)
    await state.set_state(st.Register.password)

    await message.delete()

    await message.answer("Введи пароль")


@reg.message(st.Register.password)
async def save_data(message: Message, state: FSMContext) -> str:
    await state.update_data(password=message.text)
    data = await state.get_data()
    await message.delete()

    await message.answer(f"{message.chat.first_name}, вы авторизовались")
    print(data)
    await state.clear()


# TODO: Сделать подключеие к базе и сохранение пользователя
