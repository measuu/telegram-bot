from sys import prefix

from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class ChoiseCallBack(CallbackData, prefix='choise', sep=';'):
    id: int
    name: str


def choise_keyboard_markup_astr(choise_list: list[dict], offset: int | None = None, skip: int | None = None):
    builder = InlineKeyboardBuilder()
    builder.adjust(1, repeat=True)
    for index, choise_data in enumerate(choise_list):
        callback_data = ChoiseCallBack(id=index, **choise_data)
        builder.button(text=f"{callback_data.name}", callback_data=callback_data.pack())
    builder.adjust(1, repeat=True)
    return builder.as_markup()


class ChoiseCallBack2(CallbackData, prefix='choise_2', sep=';'):
    id: int
    name: str

def choise_keyboard_markup_math(choise_list: list[dict], offset: int | None = None, skip: int | None = None):
    builder = InlineKeyboardBuilder()
    builder.adjust(1, repeat=True)
    for index, choise_data in enumerate(choise_list):
        callback_data = ChoiseCallBack2(id=index, **choise_data)
        builder.button(text=f"{callback_data.name}", callback_data=callback_data.pack())
    builder.adjust(1, repeat=True)
    return builder.as_markup()


class ChoiseCallBack3(CallbackData, prefix='choise_3', sep=';'):
    id: int
    name: str

def choise_keyboard_markup_python(choise_list: list[dict], offset: int | None = None, skip: int | None = None):
    builder = InlineKeyboardBuilder()
    builder.adjust(1, repeat=True)
    for index, choise_data in enumerate(choise_list):
        callback_data = ChoiseCallBack3(id=index, **choise_data)
        builder.button(text=f"{callback_data.name}", callback_data=callback_data.pack())
    builder.adjust(1, repeat=True)
    return builder.as_markup()