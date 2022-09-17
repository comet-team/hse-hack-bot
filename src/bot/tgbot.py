from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from src.bot.connector import Connector
from aiogram.utils import executor
import os

TOKEN = os.environ["BOT_TOKEN"]
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
connector = Connector()

# TODO давать админские права


@dp.message_handler(commands=["create"])
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

@dp.message_handler(content_types=['new_chat_members'])
async def new_user_joined(message: types.Message):
    chat = types.Chat()
    for new_member in message.new_chat_members:
        if connector.get_admin() == new_member.id:
            await chat.promote(new_member.id, can_change_info=True, can_pin_messages=True)

def start_bot():
    executor.start_polling(dp)
