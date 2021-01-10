from typing import AnyStr, NoReturn, Optional
from typing import SupportsInt as Integer

from trade_bot.db.interfaces.redis import RedisDatabase
from trade_bot.settings import config


async def save_user_access_key(
    redis: RedisDatabase, user_id: Integer, key: AnyStr,
) -> NoReturn:
    await redis.save_object_value(user_id, key)


async def check_user_access_key(
    redis: RedisDatabase, user_id: Integer,
) -> bool:
    existing_key: bytes = await redis.get_object(user_id)
    if existing_key is not None:
        if existing_key.decode() == config['bot']['access_key']:
            return True
        return False


async def delete_user_access_key(
    redis: RedisDatabase, user_id: Integer,
) -> bool:
    existing_key: bytes = await redis.get_object(user_id)
    if existing_key is not None:
        await redis.delete_object(user_id)
        return True
    return False


async def get_user_access_key(
    redis: RedisDatabase, user_id: Integer,
) -> Optional[AnyStr]:
    existing_key: bytes = await redis.get_object(user_id)
    if existing_key is not None:
        return existing_key.decode()
