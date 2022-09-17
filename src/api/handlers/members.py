from http import HTTPStatus
from aiohttp.web_response import Response
from aiohttp.web_urldispatcher import View


class MembersView(View):
    URL_PATH = r"/members"

    async def post(self) -> None:
        # data = await self.request.json()
        # chat_id = data["chatId"]
        # members = data["members"]

        return Response(status=HTTPStatus.OK)
