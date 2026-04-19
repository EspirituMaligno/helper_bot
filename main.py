import asyncio
from aiogram import Bot, Dispatcher
from src.core.config import settings
from src.core.logger_init import logger
from src.commands.start_handler import router as start_router
from src.handlers.vpn_handlers import router as vpn_hanler

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()


dp.include_router(start_router)
dp.include_router(vpn_hanler)


async def main():
    logger.info(f"Бот начал работу...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
