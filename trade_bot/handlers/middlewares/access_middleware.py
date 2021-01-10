from aiogram import Bot
from aiogram.types import Message

from types import FunctionType
from typing import Any, Callable, Dict, Tuple, Union

import trade_bot.db.actions as actions

from trade_bot.settings import config
from trade_bot.utils.logger import logger


def validate_user_access(bot: Bot) -> Callable:
    def bot_wraps(func: FunctionType) -> Callable:
        async def wrapper(
            message: Message,
            *args: Tuple[Any],
            **kwargs: Dict[Any, Any],
        ) -> Union[Any, Message]:
            logger.debug(f'Sent msg: {message.text}')
            if await actions.check_user_access_key(bot.redis, message.from_user.id):
                logger.debug(
                    f'User "{message.from_user.id}" was accessed!'
                )
                return await func(message, *args, **kwargs)

            elif message.text == config['bot']['access_key']:
                await actions.save_user_access_key(bot.redis, message.from_user.id, message.text)
                logger.debug(
                    'New was access was '
                    f'grant for user: "{message.from_user.id}"',
                )
                await bot.send_message(message.chat.id, 'Now you are accessed!')
            else:
                await bot.send_message(
                    message.chat.id,
                    'You have type an access key to act with bot!',
                )
        return wrapper
    return bot_wraps
