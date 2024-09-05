import asyncio
import logging
import sys
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.handlers import router, reg

load_dotenv()


async def main() -> None:
    bot = Bot(
        token=os.getenv("TOKEN"),  # < NOTE: Your token here in .env file >
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    dp.include_routers(router, reg)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print("Bot off")
