from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from src.connector import Connector
from aiogram.utils import executor
import os

TOKEN = os.environ["BOT_TOKEN"]
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
connector = Connector()

# TODO давать админские права

@dp.message_handler(commands=['create'])
async def create_chat(msg: types.Message):
    chat = types.Chat()
    chat.id = connector.get_chat_id()
    await chat.set_title(connector.get_chat_name())

    _, members = connector.get_chat_members()
    link = await chat.create_invite_link()
    for member_id in members:
        await bot.send_message(member_id, link.invite_link)

    admin_id = connector.get_admin()
    await bot.send_message(admin_id, link.invite_link)
    await chat.promote(admin_id, can_change_info=True, can_pin_messages=True)

def start_bot():
    executor.start_polling(dp)
