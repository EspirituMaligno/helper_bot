from aiogram.types import CallbackQuery


async def transtion_meesage_builder(topic: str, reply_kb, calld: CallbackQuery):
    msg_for_not_vpn_topic = f"Для работы с {topic} перейдите в соответствующий канал"
    await calld.message.answer(
        text=msg_for_not_vpn_topic,
        reply_markup=reply_kb,
    )
