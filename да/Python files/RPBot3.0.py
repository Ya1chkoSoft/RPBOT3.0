import os
import asyncio
from email import message
import random
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from dotenv import load_dotenv

from config import bot
from app.handlers import router
from app.database.models import async_main

bot = Bot(token=os.getenv('BOT'))
dp = Dispatcher()
test: str = "ТЕСТ ПРОЙДЕН"
     

async def main():
    load_dotenv()
    await async_main()
    dp.include_router(router)
    await dp.start_polling(bot)



if __name__ == '__main__':
    
    try:
        asyncio.run(main())
    except  KeyboardInterrupt:
        print('Exit')