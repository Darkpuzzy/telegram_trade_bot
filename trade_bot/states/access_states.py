from aiogram.utils.helper import Item

from trade_bot.states._base import BaseState


class AccessState(BaseState):
    ACCESSED = Item(value=True)
    NO_ACCESS = Item(value=False)
