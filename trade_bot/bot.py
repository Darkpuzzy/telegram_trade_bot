import asyncio

from aiogram.dispatcher import Dispatcher

from trade_bot.utils.aiogram_wrappers import Bot
from trade_bot.settings import config

TOKEN = '1458444160:AAH2dhjtcXiQuCzzKKkMdkHWXVG2wo0Thig'


def create_bot() -> Bot:
    loop = asyncio.get_event_loop()
    new_bot = Bot(token=TOKEN, loop=loop)
    new_bot = loop.run_until_complete(new_bot.connect_redis(config['db']['redis']))
    return new_bot


def create_dispatcher(bot: Bot) -> Dispatcher:
    return Dispatcher(bot)


bot: Bot = create_bot()
dispatcher: Dispatcher = create_dispatcher(bot)
