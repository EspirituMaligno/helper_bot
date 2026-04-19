from aiogram.fsm.state import State, StatesGroup


class VpnStates(StatesGroup):
    waiting_for_device_name = State()
