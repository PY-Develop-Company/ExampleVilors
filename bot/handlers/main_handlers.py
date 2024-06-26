"""
Тут варто розміщати свої обробники (хендлери) подій, команд та іншого
при роботі з ботом буде багато обробників функцій
якщо їх всі тримати в одному 1000-рядочному файлі, то в ньому буде важко розібратися
до того ж при роботі з іншими розробниками вам буде легше розуміти за що відповідає код
тому радять розділяти обробники в окремі файли по тематиці
"""

"""
До прикладу ви робите бота для для розсилання новин та листів для підписників
    1 у вас буде функціонал користувача, де він може підписати на розсилку та відписатися від неї, а також кнопки для інтеракції
    2 також буде адмін панель для менеджменту користувачів
    3 додатково у адміна є панель для створення листів(повідомлень) для надсилання
всі ці три функціонали можна розділити в окремі файли

Іноді проект є не достатньо великий і при розділенні його по різним файлам ви витратите лише більше часу
це все є інтуїтивним і тут можна самому ставити свої обмеження. Використовуйте це з розумом
я до прикладу маю правило, що файл має бути до 300 рядків
"""

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, ReplyKeyboardBuilder, KeyboardButton
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove

import bot.menu as menu
import bot.texts as texts

from bot.callbacks import InlineButton1CallbackData

# створюємо роутер, а потім його потібно підключити до диспетчера (misc.py) -> dp.include_router(router)
router = Router()


# Приклад обробника власної команди
@router.message(Command("test_command"))
async def my_command_handler(message: Message) -> None:
    await message.answer("/test_command executed!")


# Приклад створення inline menu
@router.message(Command("inline_menu_command"))
async def inline_menu_command_handler(message: Message) -> None:
    # створюємо inline markup
    markup = menu.get_inline_markup(size=5)

    # відповідаємо на повідомлення змінюючи маркап на створений нами
    await message.answer("/inline_menu_command executed!", reply_markup=markup)


# Приклад обробки натискання inline кнопок
@router.callback_query(InlineButton1CallbackData.filter())
async def inline_button1_handler(callback: types.CallbackQuery, callback_data: InlineButton1CallbackData) -> None:
    await callback.message.answer(f"Inline button {callback_data.id} pressed!")
    await callback.answer()  # для прибирання затримки в кнопці (без цього кнопка буде неактина декілька секунд)


# Приклад створення reply menu
@router.message(Command("reply_menu_command"))
async def reply_menu_command_handler(message: Message) -> None:
    # приклад створення reply menu (from markup)
    # markup = menu.reply_markup
    # приклад створення reply menu (builder)
    markup = menu.get_reply_markup()

    await message.answer("/reply_menu_command executed!", reply_markup=markup)


# приклад опрацювання reply кнопок
@router.message()
async def main_handler(message: Message) -> None:
    if message.text == texts.REPLY_BUTTON_1_TEXT:
        await message.answer("Answer for reply button 1")
    elif message.text == texts.REPLY_BUTTON_2_TEXT:
        await message.answer("Answer for reply button 2")
    elif message.text == texts.REPLY_BUTTON_3_TEXT:
        # приклад видалення reply markup
        await message.answer("Answer for reply button 3", reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer("Did not understand your command! Try again!")
