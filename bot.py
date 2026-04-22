import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from config import BOT_TOKEN
from handlers import start, loyalty, stores, manager, about, socials

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Restart / Перезапустить"),
        BotCommand(command="menu", description="Main menu / Главное меню"),
        BotCommand(command="language", description="Change language / Сменить язык"),
    ]
    await bot.set_my_commands(commands)


async def main():
    bot = Bot(token=BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(start.router)
    dp.include_router(loyalty.router)
    dp.include_router(stores.router)
    dp.include_router(manager.router)
    dp.include_router(about.router)
    dp.include_router(socials.router)

    await set_commands(bot)
    logger.info("Bot started")
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
