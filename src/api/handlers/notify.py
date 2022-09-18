from http import HTTPStatus
from aiohttp.web_response import Response
from src.bot.tgbot import send_notify
from src.api.handlers.base import BaseView


class NotifyView(BaseView):
    URL_PATH = r"/notify"

    async def post(self) -> None:
        data = await self.request.json()
        print("ok")
        chat_id = data["chat_id"]
        message = data["shedule"]
        await send_notify(chat_id, message)
        return Response(status=HTTPStatus.OK)
