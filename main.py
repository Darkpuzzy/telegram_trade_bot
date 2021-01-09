from aiogram.utils import executor

from trade_bot.bot import dispatcher
from trade_bot.handlers import access_handlers
from trade_bot.utils.logger import logger


if __name__ == '__main__':
    logger.info('Starting polling . . .')
    executor.start_polling(dispatcher)

