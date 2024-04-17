# для роботи з inline markup потрібно створювати колбеки
# у кожної з кнопок в меню (inline типу, не reply) є свій колбек, він може бути з параметрами чи без
# (його зазначають при створенні InlineKeyboardButton) (детальніше у файлі menu.py)

# при натисканні на кнопку ми можемо реагувати на цей колбек створивши хендлер з ним
# (додавши рядок @router.callback_query(CallbackDataClassExample.filter()) над функцією) (детальніше main_handers.py)

from aiogram.filters.callback_data import CallbackData


# приклад створення callback-у для inline кнопок (у кожного класу колбеку має бути унікальний prefix! І
# накше буде конфлікт і хенлери не будуть реагувати на правильний колбек)
class InlineButton1CallbackData(CallbackData, prefix="inline_button"):
    id: int # параметрів можна й не додавати. Тоді замість цього рядка пишуть pass