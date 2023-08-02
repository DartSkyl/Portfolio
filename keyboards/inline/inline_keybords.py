from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from states.user_states import types_settings, level_settings, muscle_group_settings


def type_setting_keyboard():
    inline_markup = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(text=type_name.title(), callback_data=type_name)
               for type_name in types_settings]
    inline_markup.add(*buttons)
    return inline_markup


def level_setting_keyboard():
    inline_markup = InlineKeyboardMarkup(row_width=1)
    buttons = [InlineKeyboardButton(text=type_name.title(), callback_data=type_name)
               for type_name in level_settings]
    inline_markup.add(*buttons)
    return inline_markup


def muscle_setting_keyboard():
    inline_markup = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(text=type_name.title(), callback_data=type_name)
               for type_name in muscle_group_settings]
    inline_markup.add(*buttons)
    return inline_markup
