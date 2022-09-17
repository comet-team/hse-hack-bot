import threading
import asyncio
from src.bot.tgbot import start_bot
from src.api.run_api import run
from src.instances import dp

def worker(dp, loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_bot(dp))


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    thread = threading.Thread(target=worker, args=(dp, loop))
    thread.start()
    run()
