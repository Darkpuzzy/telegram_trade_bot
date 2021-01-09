from aiogram.types import Message

from trade_bot.bot import dispatcher, bot


@dispatcher.message_handler(commands=['start'])
async def start_act_with_bot(message: Message):
    await bot.send_message(
        message.chat.id,
        f'Hello, *{message.from_user.first_name}*.\n'
        'If you want to act with me, you need '
        'to send me an *access_key*, do you have one?',
        parse_mode='markdown',
    )
