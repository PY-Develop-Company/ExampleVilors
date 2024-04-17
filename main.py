# основний файл з якого запускаємо всі інші модулі та скрипти

import asyncio
import logging
import sys

from bot.misc import main

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
