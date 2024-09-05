from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from datetime import datetime

import app.states._reg_state as st
import app.utils.logger as log

reg = Router()

# TODO: Разобраться с удалением сообщений


@reg.callback_query(F.data == "go")
async def start_handler(callback: CallbackQuery, state: FSMContext) -> str:
    await state.set_state(st.Register.login)
    await callback.message.delete()

    await callback.message.answer("Введи логин")


@reg.message(st.Register.login)
async def login_handler(message: Message, state: FSMContext) -> str:
    await state.update_data(login=message.text)
    await state.set_state(st.Register.password)

    await message.delete()

    await message.answer("Введи пароль")


@reg.message(st.Register.password)
async def save_data(message: Message, state: FSMContext) -> str:
    try:
        await state.update_data(password=message.text)

        # NOTE: Лог данных
        log.push_log(
            f"For {message.chat.id} User: {message.chat.first_name}, Password: {message.text}\n"
        )

        await message.delete()
        await message.answer(f"{message.chat.first_name}, вы авторизовались")

        await state.clear()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        await message.answer("Произошла ошибка при обработке данных.")


# TODO: Сделать подключеие к базе и сохранение пользователя
