from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


TOKEN = '1458444160:AAH2dhjtcXiQuCzzKKkMdkHWXVG2wo0Thig'


def create_bot() -> Bot:
    new_bot = Bot(token=TOKEN)
    return new_bot


def create_dispatcher(bot: Bot) -> Dispatcher:
    return Dispatcher(bot)


bot: Bot = create_bot()
dispatcher: Dispatcher = create_dispatcher(bot)
