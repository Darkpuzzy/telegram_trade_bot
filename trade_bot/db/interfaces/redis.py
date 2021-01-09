from aioredis import Redis, create_redis_pool
from aioredis.errors import ConnectionClosedError, PoolClosedError, ChannelClosedError

from typing import Any, AnyStr, Optional, TypeVar, final
from typing import SupportsInt as Integer

from trade_bot.db.interfaces._base import BaseDatabaseInterface


Self = TypeVar('Self', bound='RedisDatabase')


@final
class RedisDatabase(BaseDatabaseInterface):

    def __init__(
        self, url: AnyStr, db: Optional[Integer] = 1,
    ) -> None:
        self._redis_url = url
        self._db_number = db
        self.__pool: Optional[Redis] = None

    async def connect(self) -> Self:
        """Connect to redis pool and return self instance."""
        try:
            pool: Redis = await create_redis_pool(self._redis_url, db=self._db_number)
            await pool.ping()
            self.__pool = pool
            return self
        except (
            ConnectionError, OSError, IOError,
            PoolClosedError, ChannelClosedError, ConnectionClosedError,
        ) as err:
            raise IOError(
                f'Connection failure to Redis {self._redis_url}',
            ) from err

    async def get_object(self, key: Any) -> Any:
        """Get some object from Redis storage."""
        return await self.__pool.get(key)

    async def save_object_value(self, key: Any, value: Any) -> Any:
        """Save some value to storage with specified key."""
        return await self.__pool.set(key, value)

    async def delete_object(self, key: Any, *keys: Optional) -> Any:
        """Delete some key and containing value."""
        return await self.__pool.delete(key, *keys)

    async def update_object(self, key: Any, value: Any) -> Any:
        """Update some value in specified key."""
        if key == await self.get_object(key):
            return value
        await self.__pool.delete(key)
        return await self.__pool.set(key, value)

    async def ping(self) -> None:
        await self.__pool.ping()
