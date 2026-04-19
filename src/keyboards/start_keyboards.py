from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_start_kb():
    start_kb = [
        [InlineKeyboardButton(text="VPN", callback_data="send_start_vpn")],
    ]

    return InlineKeyboardMarkup(inline_keyboard=start_kb)
