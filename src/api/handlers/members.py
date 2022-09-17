from http import HTTPStatus
from aiohttp.web_response import Response
from src.bot.tgbot import add_members
from src.api.handlers.base import BaseView


class MembersView(BaseView):
    URL_PATH = r"/members"

    async def post(self) -> None:
<<<<<<< HEAD
        # data = await self.request.json()
        # chat_id = data["chatId"]
        # members = data["members"]

=======
        data = await self.request.json()
        chat_id = data["chatId"]
        members = data["members"]
        await add_members(chat_id, members)
>>>>>>> 0c86ea3 (feat: add /members and /admin)
        return Response(status=HTTPStatus.OK)
