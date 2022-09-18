import asyncio
from aiogram import Bot, types
from src.bot.connector import Connector
from aiogram.utils import executor
from src.instances import dp, TOKEN
from src.utils.try_dec import try_dec
from src.utils.ydisk_loader import upload, create_dir


connector = Connector()
invited_admins = set()


@try_dec()
@dp.message_handler(commands=["health"])
async def send_welcome(msg: types.Message):
    await msg.reply(f"Hey, {msg.from_user.first_name}!")


@try_dec()
@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def add_files(msg: types.Message):
    bot = Bot(token=TOKEN)
    Bot.set_current(bot)
    member = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    if member.is_chat_admin():
        file_url = await msg.document.get_url()
        path = msg.chat.full_name
        create_dir(f'{path}')
        # TODO add content types
        upload(f"{path}/{msg.document.file_name}", file_url)
    
# TODO add command for getting link of group folder with correct permissions


@try_dec()
async def create_chat(chat_id, members):
    bot = Bot(token=TOKEN)
    Bot.set_current(bot)
    chat = types.Chat()
    chat.id = chat_id
    await chat.set_title(connector.get_chat_name())
    link = await chat.create_invite_link()
    for member_id in members:
        await bot.send_message(member_id, link.invite_link)


@try_dec()
async def add_members(chat_id, members):
    bot = Bot(token=TOKEN)
    Bot.set_current(bot)
    chat = types.Chat()
    chat.id = chat_id
    link = await chat.create_invite_link()

    for member_id in members:
        await bot.send_message(member_id, link.invite_link)


@try_dec()
async def add_admin(chat_id, admin):
    bot = Bot(token=TOKEN)
    Bot.set_current(bot)
    chat = types.Chat()
    chat.id = chat_id
    link = await chat.create_invite_link()

    await bot.send_message(admin, link.invite_link)
    invited_admins.add(admin)


@try_dec()
@dp.message_handler(content_types=["new_chat_members"])
async def new_user_joined(message: types.Message):
    bot = Bot(token=TOKEN)
    Bot.set_current(bot)
    chat = types.Chat()
    chat.id = message.chat.id
    for new_member in message.new_chat_members:
        if str(new_member.id) in invited_admins:
            await chat.promote(
                new_member.id, can_change_info=True, can_pin_messages=True
            )
            invited_admins.remove(str(new_member.id))


def start_bot(dp):
    asyncio.create_task(executor.start_polling(dp))
