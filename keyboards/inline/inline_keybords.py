from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from states.paremetrs_of_choice import types_settings, level_settings, muscle_group_settings


def type_setting_keyboard():
    inline_markup = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(text=type_name, callback_data=value)
               for type_name, value in types_settings.items()]
    inline_markup.add(*buttons)
    return inline_markup


def level_setting_keyboard():
    inline_markup = InlineKeyboardMarkup(row_width=1)
    buttons = [InlineKeyboardButton(text=type_name, callback_data=value)
               for type_name, value in level_settings.items()]
    inline_markup.add(*buttons)
    return inline_markup


def muscle_setting_keyboard():
    inline_markup = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(text=type_name, callback_data=value)
               for type_name, value in muscle_group_settings.items()]
    inline_markup.add(*buttons)
    return inline_markup
