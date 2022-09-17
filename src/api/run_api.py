from aiohttp.web import run_app
from aiohttp.web_app import Application
from src.api.handlers import HANDLERS


def run() -> None:
    app = Application()
    for handler in HANDLERS:
        app.router.add_route("*", handler.URL_PATH, handler)
    run_app(app)
