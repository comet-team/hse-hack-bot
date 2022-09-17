import asyncio
from aiogram import Bot, types
from src.bot.connector import Connector
from aiogram.utils import executor
from src.instances import dp, TOKEN

connector = Connector()
invited_admins = set()

@dp.message_handler(commands=['health'])
async def send_welcome(msg: types.Message):
    await msg.reply(f'Hey, {msg.from_user.first_name}!')


async def create_chat(chat_id, members):
    bot = Bot(token=TOKEN)
    Bot.set_current(bot)
    chat = types.Chat()
    chat.id = chat_id
    await chat.set_title(connector.get_chat_name())
    link = await chat.create_invite_link()
    for member_id in members:
        await bot.send_message(member_id, link.invite_link)



async def add_members(chat_id, members):
    # TODO add decorator
    bot = Bot(token=TOKEN)
    Bot.set_current(bot)
    chat = types.Chat()
    chat.id = chat_id
    link = await chat.create_invite_link()

    for member_id in members:
        await bot.send_message(member_id, link.invite_link)


async def add_admin(chat_id, admin):
    bot = Bot(token=TOKEN)
    Bot.set_current(bot)
    chat = types.Chat()
    chat.id = chat_id
    link = await chat.create_invite_link()

    await bot.send_message(admin, link.invite_link)
    invited_admins.add(admin)


@dp.message_handler(content_types=["new_chat_members"])
async def new_user_joined(message: types.Message):
    bot = Bot(token=TOKEN)
    Bot.set_current(bot)
    chat = types.Chat()
    chat.id = message.chat.id
    for new_member in message.new_chat_members:
        if str(new_member.id) in invited_admins:
            await chat.promote(new_member.id, can_change_info=True, can_pin_messages=True)
            invited_admins.remove(str(new_member.id))

def start_bot(dp):
    asyncio.create_task(executor.start_polling(dp))
