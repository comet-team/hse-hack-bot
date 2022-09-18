import asyncio
from aiogram import Bot, types
from src.bot.connector import subscribe_to_notifications, add_user
from aiogram.utils import executor
from src.instances import dp, TOKEN
from src.utils.try_dec import try_dec
from src.utils.ydisk_loader import upload, create_dir
import time

invited_admins = set()
target_demo_chat = -1001724085725


@try_dec()
@dp.message_handler(commands=["health"])
async def check_health(msg: types.Message):
    await msg.reply(f"I'm Okey, {msg.from_user.first_name}!")


@try_dec()
@dp.message_handler(commands=["start"])
async def send_welcome(msg: types.Message):
    await msg.reply(f"Hey, {msg.from_user.first_name}!")
    print(msg.from_user.full_name)
    if msg.from_user.full_name == 'Александр Деревягин' or  \
        msg.from_user.full_name == 'Alexander Popovkin':
        print('give admin rights')
        await add_admin(target_demo_chat, msg.from_user.id)
    else:
        await add_members(target_demo_chat, [msg.from_user.id])


@try_dec()
@dp.message_handler(content_types=["document", "animation", "photo", "video", "audio"])
async def add_files(msg: types.Message):
    chat = types.Chat()
    bot = Bot(token=TOKEN)
    Bot.set_current(bot)
    member = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    print(member.is_chat_admin())
    file_url = None
    file_name = ""
    if str(msg.content_type) == 'document':
        file_url = await msg.document.get_url()
        file_name = msg.document.file_name
    elif str(msg.content_type) == 'photo':
        file_url = await msg.photo[-1].get_url()
        file_name = f'{msg.photo[-1].file_id}.jpg'
    elif str(msg.content_type) == 'video':
        file_url = await msg.video.get_url()
        file_name = msg.video.file_name
    elif str(msg.content_type) == 'animation':
        file_url = await msg.animation.get_url()
        file_name = msg.animation.file_name
    elif str(msg.content_type) == 'audio':
        file_url = await msg.audio.get_url()
        file_name = msg.audio.file_name
    path = msg.chat.full_name
    create_dir(f"{path}")
    upload(f"{path}/{file_name}", file_url)
    await bot.send_message(msg.chat.id, 'https://disk.yandex.ru/d/V2IMkj16WJzu5Q')


@try_dec()
async def send_notify(chat_id, message):
    bot = Bot(token=TOKEN)
    Bot.set_current(bot)
    print(message)
    if str(message) != str("{'error': 'zero-id-request'}"):
        chat_message = await bot.send_message(chat_id, message)
        await chat_message.pin()


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
    invited_admins.add(str(admin))
    chat = types.Chat()
    chat.id = chat_id
    link = await chat.create_invite_link()
    await bot.send_message(admin, link.invite_link)


@try_dec()
@dp.message_handler(content_types=["new_chat_members"])
async def new_user_joined(message: types.Message):
    bot = Bot(token=TOKEN)
    Bot.set_current(bot)
    chat = types.Chat()
    print(invited_admins)
    chat.id = message.chat.id
    for new_member in message.new_chat_members:
        if str(new_member.id) in invited_admins:
            await chat.promote(
                new_member.id, can_change_info=True, can_pin_messages=True
            )
            invited_admins.remove(str(new_member.id))
            await chat.set_administrator_custom_title(new_member.id, 'Преподаватель')
            await bot.send_message(message.chat.id, 'В группу добавился преподаватель!')


def start_bot(dp):
    asyncio.create_task(executor.start_polling(dp))
