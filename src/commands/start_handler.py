from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from src.core.logger_init import logger
from src.keyboards.start_keyboards import get_start_kb

router = Router()


@router.message(Command("start"))
async def command_start_handler(message: Message):
    logger.info(f"Команда /start использована: {message.from_user.username}")
    msg_for_user = "Привет! Я бот помощник"
    await message.answer(text=msg_for_user, reply_markup=get_start_kb())
