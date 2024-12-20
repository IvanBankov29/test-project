from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Callable, Dict, Any, Awaitable

class TestMiddeware(BaseMiddleware):
    """тестовый милдвейр"""
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        print('Действия для обработчика')
        result = await handler(event, data)
        print('Действия после обработчика')
        return result