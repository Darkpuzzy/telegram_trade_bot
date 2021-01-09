from aiogram import Bot as OriginBot
from typing import AnyStr, Any, TypeVar, NoReturn, Optional

from trade_bot.db import RedisDatabase

Self = TypeVar('Self', bound='Bot')


class Bot(OriginBot):
    def __init__(
        self, *args, **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self._redis: Optional[RedisDatabase] = None

    @property
    def redis(self) -> RedisDatabase:
        return self._redis

    @redis.setter
    def redis(self, value: Any) -> NoReturn:
        raise AttributeError(
            'Cannot set \'redis\' attribute!'
        )

    @redis.getter
    def redis(self) -> Optional[RedisDatabase]:
        if self._redis is None:
            try:
                raise RuntimeWarning(
                    '\'redis\' attribute is not set for \'Bot\' '
                    'you must use method \'connect_redis\'!'
                )
            finally:
                return None
        return self._redis

    async def connect_redis(self, url: AnyStr) -> Self:
        self._redis: RedisDatabase = await RedisDatabase(
            url=url,
        ).connect()
        return self
