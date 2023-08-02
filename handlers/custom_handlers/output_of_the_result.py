from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import bot

page = {'page': 1}


def exercise_list_creating(from_user_id: int):
    with bot.retrieve_data(user_id=from_user_id) as data:
        return data["exercise"]


def start_output(from_user_id: int):
    exercise_list = exercise_list_creating(from_user_id)
    page['count'] = len(exercise_list)
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=f'{page["page"]}/{page["count"]}', callback_data=' '),
               InlineKeyboardButton(text='Next - - - >', callback_data='next_page'))
    bot.send_message(from_user_id, exercise_list[0], reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ['next_page', 'back_page'])
def result_output(call):
    exercise_list = exercise_list_creating(call.from_user.id)
    page['count'] = len(exercise_list)
    markup = InlineKeyboardMarkup()
    if call.data == 'next_page':
        if page['page'] == 1 or page['page'] < len(exercise_list) - 1:
            page['page'] += 1
            markup.add(InlineKeyboardButton(text='< - - - Back', callback_data='back_page'),
                       InlineKeyboardButton(text=f'{page["page"]}/{page["count"]}', callback_data=' '),
                       InlineKeyboardButton(text='Next - - - >', callback_data='next_page'))
            bot.edit_message_text(f'{exercise_list[page["page"] - 1]}', reply_markup=markup,
                                  chat_id=call.message.chat.id, message_id=call.message.message_id)
        else:
            page['page'] += 1
            markup.add(InlineKeyboardButton(text='< - - - Back', callback_data='back_page'),
                       InlineKeyboardButton(text=f'{page["page"]}/{page["count"]}', callback_data=' '))
            bot.edit_message_text(f'{exercise_list[page["page"] - 1]}\n', reply_markup=markup,
                                  chat_id=call.message.chat.id, message_id=call.message.message_id)
    else:
        if page['page'] == 2:
            page['page'] -= 1
            markup.add(InlineKeyboardButton(text=f'{page["page"]}/{page["count"]}', callback_data=' '),
                       InlineKeyboardButton(text='Next - - - >', callback_data='next_page'))
            bot.edit_message_text(f'{exercise_list[page["page"] - 1]}\n', reply_markup=markup,
                                  chat_id=call.message.chat.id, message_id=call.message.message_id)
        else:
            page['page'] -= 1
            markup.add(InlineKeyboardButton(text='< - - - Back', callback_data='back_page'),
                       InlineKeyboardButton(text=f'{page["page"]}/{page["count"]}', callback_data=' '),
                       InlineKeyboardButton(text='Next - - - >', callback_data='next_page'))
            bot.edit_message_text(f'{exercise_list[page["page"] - 1]}', reply_markup=markup,
                                  chat_id=call.message.chat.id, message_id=call.message.message_id)
