from aiogram import Router
from aiogram.filters import Filter
from aiogram.types import Message

filter_router = Router(name="FilterRounter")


class MyFilter(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: Message) -> bool:
        return message.text == self.my_text


@filter_router.message(MyFilter("hello"))
async def my_handler(message: Message):
    await message.answer("Hello, World! (MyFilter('hello') handler executed)")
