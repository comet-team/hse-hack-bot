from http import HTTPStatus
from aiohttp.web_response import Response
from src.bot.tgbot import add_admin
from src.api.handlers.base import BaseView


class AdminView(BaseView):
    URL_PATH = r"/admin"

    async def post(self) -> None:
        data = await self.request.json()
        chat_id = data["chatId"]
        members = data["adminId"]
        await add_admin(chat_id, members)
        return Response(status=HTTPStatus.OK)
