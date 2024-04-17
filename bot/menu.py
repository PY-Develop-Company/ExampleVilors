# файл для створення ріних менюшок (або маркапів)

from aiogram.utils.keyboard import (KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardBuilder, InlineKeyboardButton,
                                    ReplyKeyboardBuilder, KeyboardButton)
import bot.texts as texts
from bot.callbacks import InlineButton1CallbackData

from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove

# Створення reply markup (буз функції)
reply_markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=texts.REPLY_BUTTON_1_TEXT),
         KeyboardButton(text=texts.REPLY_BUTTON_2_TEXT)],
        [KeyboardButton(text=texts.REPLY_BUTTON_3_TEXT)],
    ])


# Створення reply markup (функцією з використанням builder)
def get_reply_markup():
    buttons = [
        [KeyboardButton(text=texts.REPLY_BUTTON_1_TEXT),
         KeyboardButton(text=texts.REPLY_BUTTON_2_TEXT)],
        [KeyboardButton(text=texts.REPLY_BUTTON_3_TEXT)],
    ]
    builder = ReplyKeyboardBuilder(buttons)

    # перетворити builder на маркап формати list[list[InlineKeyboardButton]]
    return builder.as_markup()


# Створення inline markup (функцією з використанням builder)
def get_inline_markup(size=3):
    buttons = []
    for i in range(1, size+1):
        buttons.append(InlineKeyboardButton(text=f"Inline {i}", callback_data=InlineButton1CallbackData(id=i).pack()))
    builder = InlineKeyboardBuilder([buttons])

    # якщо потрібно перезадати максимальну кількість кнопок в першому та наступних рядках
    # (у даному випадку у першому буде 1 кнопка, а у другому та наступних по 2)
    builder = builder.adjust(1, 2)

    # є можливість об'єднувати декілька білдерів в 1
    # other_builder = InlineKeyboardBuilder([...])
    # builder.attach(other_builder)

    # це корисно коли хочемо задати унікальні формати розташування кнопок
    # наприклад увямо що маємо n-кнопок для вибору пункту у списку (по 5 в рядочку) (створюємо builder з використанням adjust(5, 5))
    # але останні дві кнопки хочемо щоб були для перемикання списку "Назад" "Далі" (2 в одному рядку) (cтворюємо інший builder з використанням adjust(2, 2))
    # потім об'єднуємо їх

    # перетворити builder на маркап формати list[list[InlineKeyboardButton]]
    return builder.as_markup()
