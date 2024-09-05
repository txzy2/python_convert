import logging

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.utils.logger as log

# import app.states._reg_state as st

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message):
    log.push_log(
        f"User {message.chat.first_name} ({message.chat.id}) starting use bot\nINFO: {message.chat}\n"
    )

    await message.answer(
        f"👋 Привет, <b>{message.from_user.full_name}</b>! Я бот для конвертации текстовых файлов.\n"
        + "Я могу конвертировать:\n<code>.docx(.doc) -> .pdf и .pdf -> .docx</code>\n"
        + "\nP.S Для теста <i><b>Lovely</b></i> тыкни на вторую кнопку 😊",
        reply_markup=kb.start,
    )


@router.message(F.text == "Привет")
async def message_handler(message: Message) -> str:
    await message.answer(f"<b>{message.from_user.full_name}</b> как дела?")


# @router.message()
# async def del_message(message: Message, state: FSMContext):
#     # Проверяем текущее состояние
#     current_state = await state.get_state()
#     print(current_state)
#     if current_state in [st.Register.login, st.Register.password]:
#         return
#     await message.delete()
