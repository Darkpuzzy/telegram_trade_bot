from aiogram.utils import executor
from aiogram.dispatcher.dispatcher import Dispatcher

from trade_bot.bot import dispatcher
from trade_bot.handlers import access_handlers
from trade_bot.utils.logger import logger


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.reset_state(user=468683995)
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    logger.info('Starting polling . . .')
    executor.start_polling(dispatcher, on_shutdown=shutdown)
