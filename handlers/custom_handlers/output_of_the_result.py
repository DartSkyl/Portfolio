from typing import Dict, List
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import bot

page: Dict[str, int] = dict()  # Dictionary is needed for turning pages with exercises


def exercise_list_creating(from_user_id: int) -> list:
    """
    Function retrieve a list of exercises from the user`s state
    :param from_user_id: User ID
    :return data["exercise"]: List of exercises
    """
    with bot.retrieve_data(user_id=from_user_id) as data:
        return data["exercise"]


def start_output(from_user_id: int) -> None:
    """
    Function starts showing exercises
    :param from_user_id: User ID
    """
    exercise_list: List[str] = exercise_list_creating(from_user_id)  # Getting a list of exercises
    page['page'] = 1  # The display always starts from the first page
    page['count'] = len(exercise_list)  # The total number of pages is the total number of exercise
    markup: InlineKeyboardMarkup = InlineKeyboardMarkup()
    # Keyboard contains two buttons: an empty one, a page display and "next"
    markup.add(InlineKeyboardButton(text=f'{page["page"]}/{page["count"]}', callback_data=' '),
               InlineKeyboardButton(text='Next - - - >', callback_data='next_page'))
    # Then this message will just change
    bot.send_message(from_user_id, exercise_list[0], reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ['next_page', 'back_page'])
def result_output(call) -> None:
    """
    Handler flipping through the pages with exercises
    :param call: Message with callback_data. Can only contain 'next_page' or  'back_page'
    """
    exercise_list: List[str] = exercise_list_creating(call.from_user.id)  # Getting a list of exercises
    page['count'] = len(exercise_list)
    # Now the keyboard can contain 3 buttons: an empty one, a page display, "next" and "back"
    markup: InlineKeyboardMarkup = InlineKeyboardMarkup()
    if call.data == 'next_page':  # Flips forward
        if page['page'] == 1 or page['page'] < len(exercise_list) - 1:  # Condition for all pages except the last one
            page['page'] += 1
            markup.add(InlineKeyboardButton(text='< - - - Back', callback_data='back_page'),
                       InlineKeyboardButton(text=f'{page["page"]}/{page["count"]}', callback_data=' '),
                       InlineKeyboardButton(text='Next - - - >', callback_data='next_page'))
            bot.edit_message_text(f'{exercise_list[page["page"] - 1]}', reply_markup=markup,
                                  chat_id=call.message.chat.id, message_id=call.message.message_id)
        else:  # If the page is the last one
            page['page'] += 1
            markup.add(InlineKeyboardButton(text='< - - - Back', callback_data='back_page'),
                       InlineKeyboardButton(text=f'{page["page"]}/{page["count"]}', callback_data=' '))
            bot.edit_message_text(f'{exercise_list[page["page"] - 1]}\n', reply_markup=markup,
                                  chat_id=call.message.chat.id, message_id=call.message.message_id)
    else:  # Flips back
        if page['page'] == 2:  # Condition for the first page
            page['page'] -= 1
            markup.add(InlineKeyboardButton(text=f'{page["page"]}/{page["count"]}', callback_data=' '),
                       InlineKeyboardButton(text='Next - - - >', callback_data='next_page'))
            bot.edit_message_text(f'{exercise_list[page["page"] - 1]}\n', reply_markup=markup,
                                  chat_id=call.message.chat.id, message_id=call.message.message_id)
        else:  # Condition for all pages except the first one
            page['page'] -= 1
            markup.add(InlineKeyboardButton(text='< - - - Back', callback_data='back_page'),
                       InlineKeyboardButton(text=f'{page["page"]}/{page["count"]}', callback_data=' '),
                       InlineKeyboardButton(text='Next - - - >', callback_data='next_page'))
            bot.edit_message_text(f'{exercise_list[page["page"] - 1]}', reply_markup=markup,
                                  chat_id=call.message.chat.id, message_id=call.message.message_id)
