import asyncio
from operator import sub
from aiogram import Bot, types
from src.bot.connector import subscribe_to_notifications
from aiogram.utils import executor
from src.instances import dp, TOKEN

invited_admins = set()


@dp.message_handler(commands=["health"])
async def send_welcome(msg: types.Message):
    await msg.reply(f"Hey, {msg.from_user.first_name}!")


@dp.message_handler(commands=["add_files"])
async def add_files(msg: types.Message):
    bot = Bot(token=TOKEN)
    await bot.get_chat_member(msg.chat.id, msg.from_user.id)


async def send_notify(chat_id, message):
    bot = Bot(token=TOKEN)
    Bot.set_current(bot)
    chat_message = await bot.send_message(chat_id, message)
    await chat_message.pin()


async def add_members(chat_id, members):
    # TODO add decorator
    bot = Bot(token=TOKEN)
    Bot.set_current(bot)
    chat = types.Chat()
    chat.id = chat_id
    link = await chat.create_invite_link()
    for member_id in members:
        await bot.send_message(member_id, link.invite_link)
    # subscribe_to_notifications(chat_id)


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
            await chat.promote(
                new_member.id, can_change_info=True, can_pin_messages=True
            )
            invited_admins.remove(str(new_member.id))


def start_bot(dp):
    asyncio.create_task(executor.start_polling(dp))
