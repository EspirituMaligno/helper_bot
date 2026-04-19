from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_transition_kb(chat_id: str, thread_id: int, message_id: int):
    inline_kb_list = [
        [
            InlineKeyboardButton(
                text="Перейти в тему",
                url=f"https://t.me/c/{chat_id}/{message_id}?thread={thread_id}",
            )
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
