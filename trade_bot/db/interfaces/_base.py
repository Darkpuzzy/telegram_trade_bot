from abc import abstractmethod
from typing import Any, Protocol


class BaseDatabaseInterface(Protocol):

    db: object = None

    @abstractmethod
    async def connect(self, *args, **kwargs) -> Any:
        raise NotImplemented()

    @abstractmethod
    async def get_object(self, key: Any) -> Any:
        raise NotImplemented()

    @abstractmethod
    async def save_object_value(self, key: Any, value: Any) -> Any:
        raise NotImplemented()

    @abstractmethod
    async def delete_object(self, key: Any) -> Any:
        raise NotImplemented()

    @abstractmethod
    async def update_object(self, key: Any, value: Any) -> Any:
        raise NotImplemented()
