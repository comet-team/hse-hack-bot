import threading
import asyncio
from src.tgbot import start_bot
from src.api.run import run

def worker(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_bot())

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    thread = threading.Thread(target=worker, args=(loop, ))
    thread.start()
    run()