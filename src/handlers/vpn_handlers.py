import os

from aiogram import F, Router
from aiogram.types import CallbackQuery, FSInputFile, Message
from aiogram.fsm.context import FSMContext


from src.handlers.transition_message import transtion_meesage_builder
from src.keyboards.vpn_keyboards import get_start_kb
from src.keyboards.transition_keyboard import get_transition_kb
from src.services.amg_service import add_vpn_user
from src.states.vpn_state import VpnStates
from src.core.config import settings


router = Router()


@router.callback_query(F.data == "send_start_vpn")
async def send_start_vpn(calld: CallbackQuery):
    msg_for_vpn_topic = (
        "Ещё раз привет, это начальное сообщение VPN\n"
        "Выпусти qr код для подключение нового устройства, по кнопке\n"
        "Для получения qr необходимо будет присвоить название"
    )
    send_msg = await calld.bot.send_message(
        chat_id=settings.CHAT_ID,
        message_thread_id=settings.VPN_THREAD_ID,
        text=msg_for_vpn_topic,
        reply_markup=get_start_kb(),
    )
    if calld.message.message_thread_id != 2:
        trans_kb = get_transition_kb(
            chat_id=str(send_msg.chat.id)[4:],
            thread_id=send_msg.message_thread_id,
            message_id=send_msg.message_id,
        )
        await transtion_meesage_builder(topic="VPN", reply_kb=trans_kb, calld=calld)


@router.callback_query(F.data == "generate_qr_by_user")
async def input_name(calld: CallbackQuery, state: FSMContext):
    msg_for_input = "Введи название нового устройства. Например: vlad_phone"
    await calld.message.answer(text=msg_for_input)
    await state.set_state(VpnStates.waiting_for_device_name)


@router.message(VpnStates.waiting_for_device_name)
async def handle_device_name(message: Message, state: FSMContext):
    device_name = message.text
    await state.clear()

    await message.answer(f"Генерирую QR для устройства: {device_name}...")

    path_dict = add_vpn_user(device_name)

    await message.answer_photo(
        FSInputFile(path_dict["qr_path"]), caption=f"VPN для {device_name}"
    )
    await message.answer_document(FSInputFile(path_dict["conf_path"]))
    os.remove(path_dict["qr_path"])
