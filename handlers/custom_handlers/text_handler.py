from telebot.types import Message
from loader import bot
from keyboards.inline.inline_keybords import type_setting_keyboard, level_setting_keyboard


@bot.message_handler(content_types='text')
def type_setting(message: Message):
    if message.text == 'Выбрать тип тренировки':
        bot.send_message(message.chat.id, 'Выберете тип тренировки:',
                         reply_markup=type_setting_keyboard())
    elif message.text == 'Установить уровень тренировки':
        bot.send_message(message.chat.id, 'Выберете тип тренировки:',
                         reply_markup=level_setting_keyboard())
