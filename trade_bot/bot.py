import asyncio

from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage

from trade_bot.utils.aiogram_wrappers import Bot
from trade_bot.settings import config

TOKEN = '1458444160:AAH2dhjtcXiQuCzzKKkMdkHWXVG2wo0Thig'


def create_bot() -> Bot:
    loop = asyncio.get_event_loop()
    new_bot = Bot(token=TOKEN, loop=loop)
    new_bot = loop.run_until_complete(
        new_bot.connect_redis(config['db']['redis']['url']),
    )
    return new_bot


def create_dispatcher(bot: Bot) -> Dispatcher:
    return Dispatcher(
        bot,
        loop=bot.loop,
        storage=RedisStorage(
            loop=bot.loop,
            host=config['db']['redis']['host'],
            port=config['db']['redis']['port'],
            password=config['db']['redis']['password'],
        ),
    )


bot: Bot = create_bot()
dispatcher: Dispatcher = create_dispatcher(bot)
