from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

start = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="😍 Летс гиря", callback_data="go")],
        [
            InlineKeyboardButton(
                text="Lovely", web_app=WebAppInfo(url="https://lovely1337.netlify.app")
            )
        ],
    ]
)
