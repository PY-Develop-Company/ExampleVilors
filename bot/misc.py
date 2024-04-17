# основний файл бота, в якому його запускають

import config

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from bot.handlers.main_handlers import router


# Створюємо об'єкт диспетчера. Диспатчер - це головний рутер. Рутер - це об'єкт який реєструє всі хендлери.
dp = Dispatcher()

# Всі рутери мають бути прив'язані до диспатчера. Інакше їхні хендлери не спрацюють.
# Часто при великих проектах зручно розділити хендлери на декілка скриптів. Там і приходять на допомогу рутери.


# Прив'язування рутера до хендлера.
dp.include_router(router)

# Порядок приєднання рутерів має значення. Першими перевірятимуться хенлери диспетчера, а потім всі рутери в порядку
# приєднання. Тобто якщо у вас у рутері та диспетчері є звичайний echo handler (без інших фільрів та умов),
# то виконається лише той, що у диспетчера.


# ініціалізуємо об'єкт бота з токеном створени у @BotFather
# парс мод задавати не обов'язково. Він зазначає яким чином форматувати повідомлення
bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)


# хендлер команди /start
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    answer_text = (
        f"Hello, {hbold(message.from_user.full_name)}!\n"
        f"commands: /test_command, /inline_menu_command, /reply_menu_command")

    # відвповідь на повідомлення користувача (спосіб 1 - найкращий)
    await message.answer(answer_text)

    # відвповідь на повідомлення користувача (спосіб 2 - коли нема message, але маємо лише chat_id)
    # chat_id = message.chat.id
    # await bot.send_message(chat_id, answer_text)


async def main() -> None:
    # для ігнорування івентів (повідомлень, натискань на кнопки і тд.) зроблених під час неактивності бота
    await bot.delete_webhook(drop_pending_updates=True)
    # запускаємо бота через long pooling mode диспатчера
    await dp.start_polling(bot)
