import os
import json
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import bot
from ..default_handlers.start import bot_start
from states.paremetrs_of_choice import *

page_dict = {'page': 1}


@bot.callback_query_handler(func=lambda call: call.data in types_settings.values())
def setting_choice(call):
    for type_name, value in types_settings.items():
        if call.data == value:
            setting_dict['type'] = type_name
            request_dict['type'] = value
    bot_start(call.message)


@bot.callback_query_handler(func=lambda call: call.data in level_settings.values())
def setting_choice(call):
    for type_name, value in level_settings.items():
        if call.data == value:
            setting_dict['difficulty'] = type_name
            request_dict['difficulty'] = value
    bot_start(call.message)


@bot.callback_query_handler(func=lambda call: call.data in muscle_group_settings.values())
def setting_choice(call):
    for type_name, value in muscle_group_settings.items():
        if call.data == value:
            setting_dict['muscle'] = type_name
            request_dict['muscle'] = value
    bot_start(call.message)


@bot.callback_query_handler(func=lambda call: call.data in ['next_page', 'back_page'])
def page_scroll(call):
    with open(os.path.join('ready_answer.json'), 'r') as file:
        exercise_list = json.load(file)
    page_dict['count'] = len(exercise_list)
    markup = InlineKeyboardMarkup()
    if call.data == 'next_page':
        if page_dict['page'] < page_dict['count']:
            page_dict['page'] += 1
            markup.add(InlineKeyboardButton(text='< - - - Назад', callback_data='back_page'),
                       InlineKeyboardButton(text=f'{page_dict["page"]}/{page_dict["count"]}', callback_data=' '),
                       InlineKeyboardButton(text='Вперед - - - >', callback_data='next_page'))
            bot.edit_message_text(f'{exercise_list[page_dict["page"] - 1]}\n'
                                  f'Упражнение {page_dict["page"]} из {page_dict["count"]}', reply_markup=markup,
                                  chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif call.data == 'back_page':
        if page_dict['page'] > 1:
            page_dict['page'] -= 1
            markup.add(InlineKeyboardButton(text='< - - - Назад', callback_data='back_page'),
                       InlineKeyboardButton(text=f'{page_dict["page"]}/{page_dict["count"]}', callback_data=' '),
                       InlineKeyboardButton(text='Вперед - - - >', callback_data='next_page'))
            bot.edit_message_text(f'{exercise_list[page_dict["page"] - 1]}\n'
                                  f'Упражнение {page_dict["page"]} из {page_dict["count"]}', reply_markup=markup,
                                  chat_id=call.message.chat.id, message_id=call.message.message_id)
