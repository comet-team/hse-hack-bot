from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from connector import Connector
import os

TOKEN = os.environ['BOT_TOKEN']
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
connector = Connector()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    print(msg.chat)
    await msg.reply(f'Я бот. Приятно познакомиться {msg.from_user.first_name}')

@dp.message_handler(commands=['create'])
async def create_chat(msg: types.Message):
    chat = types.Chat()
    chat.id = connector.get_chat_id()
    await chat.set_title(connector.get_chat_name())
    link = await chat.create_invite_link()
    await msg.reply(link.invite_link)


if __name__ == '__main__':
   executor.start_polling(dp)
