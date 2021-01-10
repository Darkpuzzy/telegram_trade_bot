from aiogram.types import Message
from aiogram.dispatcher.storage import FSMContext

from typing import AnyStr, Optional

from trade_bot.utils.logger import logger
from trade_bot.bot import dispatcher, bot
from trade_bot.states.access_states import AccessState
from trade_bot.db.actions import action_save_user_access_key as action
from trade_bot.settings import config


@dispatcher.message_handler(state=AccessState.NO_ACCESS)
async def check_user_access(message: Message, state: FSMContext) -> None:
    if await action.check_user_access_key(bot.redis, message.from_user.id):
        logger.debug(f'User "{message.from_user.id}" was accessed!')
        await state.finish()
        await state.set_state(AccessState.ACCESSED)
        return await state.finish()

    elif message.text == config['bot']['access_key']:
        # TODO: Refactor this code to save random access key or based on hashes
        logger.debug(
            f'User "{message.from_user.id}" was '
            f'accessed with valid access_key: "{message.text}"!',
        )
        await action.save_user_access_key(bot.redis, message.from_user.id, message.text)
        await state.set_state(AccessState.ACCESSED)
        await message.answer('Now you are accessed\!')
        return await state.finish()

    else:
        await message.answer(
            'You have type an *access key* to act with bot\!',
            parse_mode='MarkdownV2'
        )
        return await state.set_state(AccessState.NO_ACCESS)


@dispatcher.message_handler(commands='start')
async def start_act_with_bot(message: Message) -> Message:
    logger.debug(f'User started acting with bot: "{message.from_user.id}"')
    state: FSMContext = dispatcher.current_state(user=message.from_user.id)

    if await state.get_state(None):
        return await message.answer(
            f'You have already */start*\'ed acting with bot.'
        )
    await state.set_state(AccessState.NO_ACCESS)
    await message.answer(
        f'Hello, *{message.from_user.first_name}*.\n'
        'If you want to act with me, you need '
        'to send me an *access_key*, do you have one?',
        parse_mode='markdown',
    )


@dispatcher.message_handler(commands='revoke')
async def revoke_key(message: Message) -> None:
    state: FSMContext = dispatcher.current_state(user=message.from_user.id)
    if key := await action.get_user_access_key(  # type: AnyStr
        bot.redis, message.from_user.id,
    ):
        await action.delete_user_access_key(bot.redis, message.from_user.id)
        logger.debug(
            f'Key ({key}) was revoked for user: "{message.from_user.id}".'
        )
        await message.answer(f'Your key _\({str().join(key.split("-"))}\)_  was revoked\!')
        await state.set_state(AccessState.NO_ACCESS)
    else:
        await message.answer(
            'You are have not *any access key*\!', parse_mode='MarkdownV2'
        )

