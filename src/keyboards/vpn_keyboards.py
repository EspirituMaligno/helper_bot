from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_start_kb():
    inline_kb_list = [
        [
            InlineKeyboardButton(
                text="Выпустить qr", callback_data="generate_qr_by_user"
            )
        ],
    ]

    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
