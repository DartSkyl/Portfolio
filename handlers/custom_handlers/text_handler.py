from telebot.types import Message
from loader import bot
from keyboards.inline.inline_keybords import type_setting_keyboard, level_setting_keyboard, muscle_setting_keyboard
from states.paremetrs_of_choice import setting_dict


@bot.message_handler(content_types='text')
def type_setting(message: Message):
    if message.text == 'Выбрать тип тренировки':
        bot.send_message(message.chat.id, f'Выберете тип тренировки:\n{message.id}',
                         reply_markup=type_setting_keyboard())
    elif message.text == 'Установить уровень тренировки':
        bot.send_message(message.chat.id, 'Выберете уровень тренировки:',
                         reply_markup=level_setting_keyboard())
    elif message.text == 'Выбрать группу мышц':
        bot.send_message(message.chat.id, 'Выберете группу мышц:',
                         reply_markup=muscle_setting_keyboard())
    elif message.text == 'Посмотреть упражнения':
        if len(setting_dict) < 3:
            if setting_dict.get('type') is None:
                bot.send_message(message.chat.id, 'Нужно выбрать тип тренировки')
            if setting_dict.get('level') is None:
                bot.send_message(message.chat.id, 'Нужно установить уровень тренировки')
            if setting_dict.get('muscle') is None:
                bot.send_message(message.chat.id, 'Нужно выбрать группу мышц')
        else:
            bot.send_message(message.chat.id, 'Все работает!')
