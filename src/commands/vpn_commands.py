from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(Command("vpn_func"))
async def get_vpn_start_message(message: Message):
    pass
