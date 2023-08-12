from typing import List
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from states.user_states import types_settings, level_settings, muscle_group_settings


def type_setting_keyboard() -> InlineKeyboardMarkup:
    """Function returns the keyboard to select the type of workout"""
    inline_markup: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=2)
    buttons: List[InlineKeyboardButton] = [InlineKeyboardButton(text=type_name.title(), callback_data=type_name)
                                           for type_name in types_settings.keys()]
    inline_markup.add(*buttons)
    return inline_markup


def level_setting_keyboard() -> InlineKeyboardMarkup:
    """Function returns the keyboard to select the training level"""
    inline_markup: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=1)
    buttons: List[InlineKeyboardButton] = [InlineKeyboardButton(text=type_name.title(), callback_data=type_name)
                                           for type_name in level_settings.keys()]
    inline_markup.add(*buttons)
    return inline_markup


def muscle_setting_keyboard() -> InlineKeyboardMarkup:
    """Function returns a keyboard for selecting a muscle group"""
    inline_markup: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=2)
    buttons: List[InlineKeyboardButton] = [InlineKeyboardButton(text=type_name.title(), callback_data=type_name)
                                           for type_name in muscle_group_settings.keys()]
    inline_markup.add(*buttons)
    return inline_markup
