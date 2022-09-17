from aiogram import Bot
import os
from aiogram.dispatcher import Dispatcher

TOKEN = os.environ["BOT_TOKEN"]
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
