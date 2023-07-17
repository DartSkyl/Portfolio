import os
import json
from telebot.types import Message
from loader import bot
from keyboards.inline.inline_keybords import *
from states.paremetrs_of_choice import setting_dict
from utils.workout_api import edit_func


@bot.message_handler(content_types='text')
def type_setting(message: Message):
    if message.text == 'Выбрать тип тренировки':
        bot.send_message(message.chat.id, f'Выберете тип тренировки:\n',
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
            if setting_dict.get('difficulty') is None:
                bot.send_message(message.chat.id, 'Нужно установить уровень тренировки')
            if setting_dict.get('muscle') is None:
                bot.send_message(message.chat.id, 'Нужно выбрать группу мышц')
        else:
            edit_func()
            with open('ready_answer.json', 'r') as file:
                exercise_list = json.load(file)
            page_dict = {'count': len(exercise_list), 'page': 1}
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton(text=f'{page_dict["page"]}/{page_dict["count"]}', callback_data=' '),
                       InlineKeyboardButton(text='Вперед - - - >', callback_data='next_page'))
            bot.send_message(message.chat.id, exercise_list[0], reply_markup=markup)

if __name__ == '__main__':
    with open(os.path.join('..', '..', 'states', 'ready_answer.json'), 'r') as file:
        exercise_list = json.load(file)
    print(exercise_list)
